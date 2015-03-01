from django.db import models


ARCHERY_TYPES = (
    ('I', 'Indoor Target'),
    ('O', 'Outdoor Target'),
    ('F', 'Field'),
    ('C', 'Clout'),
    ('W', 'Wand'),
    ('L', 'Flight'),
    ('H', 'Other'),
    ('M', 'Mixed'),
)


class Region(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=63)

    def __str__(self):
        return self.short_name


class County(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=63)
    region = models.ForeignKey(Region, blank=True, null=True)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = 'counties'


class Club(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=63)
    county = models.ForeignKey(County, blank=True, null=True)

    def __str__(self):
        return self.short_name


class Round(models.Model):
    name = models.CharField(max_length=255)
    shoot_type = models.CharField(max_length=1, choices=ARCHERY_TYPES)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'series'


class Tournament(models.Model):
    RECORD_STATUSES = (
        ('None', 'No record status'),
        ('UKRS', 'UK record status'),
        ('WRS', 'World record status'),
        ('Rose', 'Rose & UK record status'),
        ('AH', 'Arrowhead'),
        ('Tassel', 'Tassel status'),
        ('TUKRS', 'Tassel & UK record status'),
    )

    STATUS_CHOICES = (
        ('listed', 'Listed'),
        ('open', 'Entries open'),
        ('full', 'Full'),
        ('ongoing', 'Happening now'),
        ('past', 'Completed'),
    )

    name = models.CharField(max_length=511)
    start_date = models.DateField()
    end_date = models.DateField()

    organising_club = models.ForeignKey(Club, blank=True, null=True)
    organising_county = models.ForeignKey(County, blank=True, null=True)
    series = models.ForeignKey(Series, blank=True, null=True)

    status = models.CharField(max_length=31, choices=STATUS_CHOICES)
    shoot_type = models.CharField(max_length=1, choices=ARCHERY_TYPES)
    record_status = models.CharField(max_length=7, choices=RECORD_STATUSES)
    rounds = models.ManyToManyField(Round)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def organiser(self):
        return self.organising_club or self.organising_county

    @property
    def has_record_status(self):
        return not self.record_status == 'None'
