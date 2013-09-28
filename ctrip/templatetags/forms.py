from django import template
from django.forms import Form
from django.conf import settings

from ctrip.forms.trip_forms import TripForm

register = template.Library()
supported = dict(settings.LANGUAGES)

def form(context, form_name):
    request = context['request']

    if 'form' not in context or context['form'] is None:
        if form_name:
            g = globals()
            if form_name in g and issubclass(g[form_name], Form):
                form = g[form_name](request=request, context=context)
            else:
                raise KeyError('reference to an undefined form %s' % form_name)
        else:
            form = None
    else:
        form = context['form']

    return locals()
form = register.inclusion_tag('form.html',
                              takes_context=True)(form)
