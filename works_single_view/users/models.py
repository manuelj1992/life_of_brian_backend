from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Contributors(models.Model):
    name = CharField(_("Name of Contributors"), blank=True, max_length=255)

    def __str__(self):
        return self.name


class WorksSingle(models.Model):
    title = CharField(_("Work title"), blank=True, max_length=255)
    iswc = CharField(_("International Standard Musical Work Code"), blank=True, max_length=255)
    source = CharField(_("Metadata provider"), blank=True, max_length=255)
    md_id = CharField(_("Metadata provider"), blank=True, max_length=255)
    contributors = models.ManyToManyField('Contributors')

    def __str__(self):
        return self.title
