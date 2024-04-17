from django.conf import settings
from django.db import models


# Create your models here.
class Event(models.Model):
    CONCERT = 'CT'
    CONFERENCE = 'CE'
    GAME = 'G'

    CATEGORY_CHOICES = [
        (CONCERT, 'Concert'),
        (CONFERENCE, 'Conference'),
        (GAME, 'Game')
    ]

    name = models.CharField(max_length=255)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    description = models.TextField()
    attendees = models.CharField(max_length=255)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f'{self.name} - {self.date} - {self.time}'

    def list_category(self):
        return ', '.join(category.name for category in self.category.all()[:2])


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    RESERVED = 'R'
    CANCELLED = 'C'
    PENDING = 'P'
    STATUS_CHOICES = [
        (RESERVED, 'Reserved'),
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending')
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    attendee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=RESERVED)

    def __str__(self):
        return f'{self.name} - {self.event}-{self.status}'
