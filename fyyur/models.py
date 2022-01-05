from django.db import models


# Create your models here.

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=500)
    city = models.TextField(max_length=500)
    state = models.TextField(max_length=500)
    address = models.TextField(max_length=500)
    genres = models.TextField(max_length=1000, null=True)
    phone = models.TextField(max_length=100, null=True)
    image_link = models.TextField(max_length=1000)
    facebook_link = models.TextField(max_length=1000, null=True)
    website = models.TextField(max_length=1000, null=True)
    seekingTalent = models.BooleanField(default=False)
    seekingDescription = models.TextField(max_length=1000, null=True)

    class Meta:
        verbose_name_plural = "Venue"
        db_table = "venue"


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=1000)
    city = models.TextField(max_length=1000)
    state = models.TextField(max_length=1000)
    genres = models.TextField(max_length=1000)
    phone = models.TextField(max_length=100, null=True)
    image_link = models.TextField(max_length=1000)
    facebook_link = models.TextField(max_length=1000, null=True)
    website = models.TextField(max_length=1000, null=True)
    seekingVenue = models.BooleanField(default=False, null=True)
    seekingDescription = models.TextField(max_length=1000, null=True)

    class Meta:
        verbose_name_plural = "Artist"
        db_table = "artist"


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue')
    start_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Show"
        db_table = "show"

