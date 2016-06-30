from django.conf.urls import url
from concertowl import views

urlpatterns = [
    url(r'^upload_json/$', views.upload_json, name='upload_json'),
    url(r'^provide_tool/$', views.ToolView.as_view(), name='provide_tool'),
    url(r'^spotify/$', views.spotify, name='spotify'),
    url(r'^show_artists/$', views.ArtistsView.as_view(), name='show_artists'),
    url(r'^show_records/$', views.RecordsView.as_view(), name='show_records'),
    url(r'^add_artists/$', views.AddArtistsView.as_view(), name='add_artists'),
    url(r'^recommendations/$', views.RecommendationsView.as_view(), name='recommendations'),
    url(r'^$', views.EventsView.as_view(), name='show_events'),
]