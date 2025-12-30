# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Department(models.Model):

    #__Department_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    glp = models.BooleanField()
    facility = models.CharField(max_length=255, null=True, blank=True)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")


class Instrument(models.Model):

    #__Instrument_FIELDS__
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    label = models.ForeignKey(InstrumentLable, on_delete=models.CASCADE)

    #__Instrument_FIELDS__END

    class Meta:
        verbose_name        = _("Instrument")
        verbose_name_plural = _("Instrument")


class Instrumentlable(models.Model):

    #__Instrumentlable_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Instrumentlable_FIELDS__END

    class Meta:
        verbose_name        = _("Instrumentlable")
        verbose_name_plural = _("Instrumentlable")



#__MODELS__END
