from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Contributors(models.Model):
    name = models.CharField(_("Name"), blank=True, max_length=255)

    def __str__(self):
        return self.name


class Single(models.Model):
    title = models.CharField(_("Work title"), blank=True, max_length=255)
    iswc = models.CharField(_("International Standard Musical Work Code"), blank=True, max_length=255)
    others_title = models.CharField(_("Work others title"), blank=True, null=True, max_length=255)

    def __str__(self):
        return '%s - %s' % (self.title, self.iswc)


class Source(models.Model):
    name = models.CharField(_("Metadata provider"), blank=True, max_length=255)

    def __str__(self):
        return self.name


class SourceSingle(models.Model):
    md_id = models.CharField(_("Metadata provider id"), blank=True, max_length=255)
    single = models.ForeignKey('Single', on_delete=models.CASCADE, blank=True)
    source = models.ForeignKey('Source', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.single.title, self.source.name, self.md_id)


class WorksSingle(models.Model):
    source = models.ForeignKey('SourceSingle', on_delete=models.CASCADE, blank=True)
    contributors = models.ManyToManyField('Contributors', related_name='original')
    others_contributors = models.ManyToManyField('Contributors', related_name='others')

    def __str__(self):
        return '%s - %s - %s' % (self.source.single.title, self.source.source.name, self.source.md_id)
