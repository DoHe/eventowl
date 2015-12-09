from eventowl.app_previews import AbstractPreview
from concertowl import models
from eventowlproject.settings import NUMBER_OF_PREVIEW_OBJECTS


class Preview(AbstractPreview):
    
    @staticmethod
    def description():
        return "concerts close to you"
    
    @staticmethod
    def get_objects(options):
        city = options['city']
        country = options['country']
        previews = models.Preview.objects.filter(city=city,
                                                 country=country)
        return previews.order_by('-updated_at')[:NUMBER_OF_PREVIEW_OBJECTS]