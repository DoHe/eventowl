from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.name)

class Event(models.Model):
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    ticket_url = models.URLField()
    artists = models.CharField(max_length=500)

    def __unicode__(self):
        name = u"{} at {} on {}".format(unicode(self.artists),
                                        unicode(self.venue),
                                        unicode(self.date.strftime("%Y-%m-%d")))
        return name
