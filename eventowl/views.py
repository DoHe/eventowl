from datetime import date, timedelta

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import FormView
from account.mixins import LoginRequiredMixin
from account import views as account_views

from eventowl.models import UserProfile
from eventowl.forms import SignupForm, SettingsForm

from pyconcertproject import settings

class ChoiceView(TemplateView):
    template_name = 'eventowl/choice.html'

class CustomListView(LoginRequiredMixin, ListView):
    paginate_by = settings.PAGINATION_SIZE

    def _filtered_and_sorted(self, name_filter, user):
        raise NotImplementedError

    def get_queryset(self):
        name_filter = self.request.GET.get("filter", "")
        return self._filtered_and_sorted(name_filter, self.request.user)


class EventsView(CustomListView):
    template_name = None
    context_object_name = 'events'
    event_model = None
    originator_model = None
    originator_name = None

    def _filtered_and_sorted(self, name_filter, user):
        subscribed_originators = self.originator_model.objects.filter(subscribers=user,
                                                                      name__icontains=name_filter)

        oldest_shown = date.today() - timedelta(days=settings.DAYS_BACK)

        kwargs = {self.originator_name + '__in': subscribed_originators,
                  'date__gte': oldest_shown}
        subscribed_events = self.event_model.objects.filter(**kwargs)
        return subscribed_events.order_by("date")


class AddView(LoginRequiredMixin, TemplateView):
    template_name = None

    def get(self, request):
        add_originator = request.GET.get("add")
        if add_originator is not None:
            self.update_func([add_originator], request.user)
        return TemplateView.get(self, request)


class OriginatorView(CustomListView):
    template_name = None
    context_object_name = None
    unsubscribe_func = None
    favorite_func = None
    unfavorite_func = None
    originator_model = None
    order_by = 'name'

    def get(self, request):
        unsubscribe = request.GET.get("remove")
        if unsubscribe is not None:
            self.unsubscribe_func(unsubscribe, request.user)

        favorite = request.GET.get("favorite")
        if favorite is not None:
            self.favorite_func(favorite, request.user)

        unfavorite = request.GET.get("unfavorite")
        if unfavorite is not None:
            self.unfavorite_func(unfavorite, request.user)

        return CustomListView.get(self, request)

    def get_context_data(self, **kwargs):
        context = CustomListView.get_context_data(self, **kwargs)
        context['favorites'] = self.originator_model.objects.filter(favoritedby=self.request.user)
        return context

    def _filtered_and_sorted(self, name_filter, user):
        subscribed_originators = self.originator_model.objects.filter(subscribers=user,
                                                                      name__icontains=name_filter)
        return subscribed_originators.order_by(self.order_by)


class ImpressumView(TemplateView):
    template_name = 'eventowl/impressum.html'


class AboutView(TemplateView):
    template_name = 'eventowl/about.html'


class SignupView(account_views.SignupView):
    form_class = SignupForm

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        profile, created = UserProfile.objects.get_or_create(user=self.created_user,
                                                             city=form.cleaned_data["city"])
        if created:
            profile.save()


class SettingsView(FormView):
    template_name = 'account/settings.html'
    form_class = SettingsForm
    success_url = '/account/settings'

    def get_initial(self):
        initial = super(SettingsView, self).get_initial()
        initial['email'] = self.request.user.email
        initial['city'] = self.request.user.userprofile.city
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.email = form.cleaned_data['email']

        old_city = user.userprofile.city
        new_city = form.cleaned_data['city']
        user.userprofile.city = new_city

        user.save()
        user.userprofile.save()

        if old_city != new_city:
            subscribed_artists = [artist.name for artist in user.artists.all()]
            update_events(subscribed_artists, [new_city])  # TODO: do in subclass 

        return super(SettingsView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(SettingsView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
