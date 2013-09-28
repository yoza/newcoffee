"""
Campaign templatetags

"""

from django.conf import settings
from django import template
from django.views.decorators.cache import never_cache

from ctrip.models import Trip

register = template.Library()


@never_cache
@register.inclusion_tag('ctrip/trip_form.html', takes_context=True)
def trip_form(context):
    """
    add departures
    """

    if 'request' in context:
        request = context['request']
    if 'slug' in context:
        slug = context['slug']
    form = None
    formset = None
    if 'form' in context:
        form = context['form']
    if 'form' in context:
        formset = context['formset']
    return locals()


@never_cache
@register.inclusion_tag('ctrip/trip_list.html', takes_context=True)
def trip_list(context):
    """
    show personal campaigns
    """
    if 'request' in context:
        request = context['request']
        trips = \
            Trip.objects.all().order_by('name')

        return {'trips': trips,
                'request': request}
