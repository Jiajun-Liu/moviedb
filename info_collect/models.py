from django.db import models
#from json_field import JSONField
from dal import autocomplete


# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ProdCompany(models.Model):
    name = models.CharField(max_length=64)
    capital = models.CharField(max_length=32)
    location = models.TextField(max_length=128)
    scope = models.TextField(max_length=512, default=None)
    industry = models.TextField(max_length=128, default=None)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Duty(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=32)
    year = models.IntegerField()
    boxoffice = models.FloatField()

    def __unicode__(self):
        return '%s - %d - %.1f' % (self.title, self.year, self.boxoffice)

    def __str__(self):
        return '%s - %d - %.1f' % (self.title, self.year, self.boxoffice)


class ProducerMovieDuty(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    company = models.ForeignKey(ProdCompany, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.producer.name, self.movie.title, self.duty.name, self.company.name if
        self.company else None)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.producer.name, self.movie.title, self.duty.name, self.company.name if
        self.company else None)

    class Meta:
        unique_together = ("producer", "movie", 'duty')


class CompanyMovieDuty(models.Model):
    company = models.ForeignKey(ProdCompany, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s, %s, %s' % (self.company.name, self.movie.title, self.duty.name)

    def __str__(self):
        return '%s, %s, %s' % (self.company.name, self.movie.title, self.duty.name)

    class Meta:
        unique_together = ("company", "movie", 'duty')
