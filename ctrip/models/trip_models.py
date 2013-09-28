# -*- coding: UTF-8 -*-
"""
coffeetrip models

"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone


class Trip(models.Model):
    """
    trip model
    """
    name = models.CharField(_('name'), max_length=255,
                            help_text=_('Trip name'))
    slug = models.SlugField(_('slug'), null=False, blank=False, max_length=128,
                            unique=True, help_text=_('Trip slug'))

    class Meta:
        verbose_name = _('trip')
        verbose_name_plural = _('trips')
        app_label = settings.APP_LABEL
        db_table = u'trip'

    def __unicode__(self):
        return self.name

    def get_url(self):
        """
        prepare base url
        """
        return "trip/%s/" % self.slug


class Departure(models.Model):
    """
    departure model
    """
    trip = models.ForeignKey(Trip, verbose_name=_('trip'))
    start_date = models.DateTimeField(_('start date'), default=timezone.now())

    class Meta:
        verbose_name = _('departure')
        verbose_name_plural = _('departures')
        app_label = settings.APP_LABEL
        db_table = u'departure'
