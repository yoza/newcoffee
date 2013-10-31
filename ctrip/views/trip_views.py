"""
Views for coffee trips
"""
from __future__ import absolute_import
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.shortcuts import render
from django.utils import simplejson
from django.utils.safestring import mark_safe

from ctrip.models import Trip, Departure
from ctrip.forms.trip_forms import TripForm, DepartureInlineForm


@never_cache
@require_POST
@csrf_protect
def delete_trip_view(request):
    """
    delete trips
    """

    context = RequestContext(request)
    post_reset_redirect = reverse('trip-view', kwargs={})

    if request.method == 'POST' and request.is_ajax():
        data = request.POST.copy()
        values = []
        new_url = ''
        for item in data:
            if 'trip' in item.split('-')[0]:
                values.append(item.split('-')[1])
        if len(values):
            slugs = []
            try:
                trips = Trip.objects.filter(id__in=values)
                for trip in trips:
                    slugs.append(trip.slug)

                trips.delete()
            except Trip.DoesNotExist:
                pass
            """
            there we are check if cureent trip is active
            if yes: reload page after return json,
            if no: return json results with list of trips
            """
            slug = data.get('slug', '')
            if slug and slug in slugs:
                new_url = post_reset_redirect

            trips = Trip.objects.all().order_by('name')
            context = {'trips': trips,
                       'request': request}
            trip_html = \
                render_to_string('ctrip/trip_list.html',
                                 context,
                                 context_instance=RequestContext(request))
            json = {
                'html': trip_html,
                'success': True,
                'new_url': new_url
            }
            json_response = simplejson.dumps(json)
            return HttpResponse(json_response, mimetype="application/json")

        return HttpResponseRedirect(post_reset_redirect)
    else:
        trips = Trip.objects.all().order_by('name')

        template_vars = {'trips': trips,
                         'request': request}

    return render(request, 'ctrip/trip_list.html', template_vars)


@never_cache
@csrf_protect
def trip_view(request, slug='', form_class=None):
    """
    trip view
    """

    try:
        trp = Trip.objects.get(slug=slug)
    except Trip.DoesNotExist:
        trp = Trip()

    trip_formset = inlineformset_factory(Trip,
                                         Departure,
                                         form=DepartureInlineForm,
                                         can_delete=True,
                                         fk_name='trip',
                                         extra=1)

    if form_class is None:
        form_class = TripForm

    if request.method == "POST":
        form = form_class(data=request.POST.copy(),
                          files=request.FILES,
                          request=request,
                          instance=trp)
        formset = trip_formset(request.POST, request.FILES, instance=trp)

        if form.is_valid() and formset.is_valid():
            for item in trp.__dict__:
                if item in form.cleaned_data:
                    trp.__setattr__(item, form.cleaned_data[item])

            trp.save()
            formset.save()
            _kwargs = {}
            if form.cleaned_data['slug']:
                _kwargs = {'slug': form.cleaned_data['slug']}
            post_reset_redirect = reverse('trip-view', kwargs=_kwargs)

            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = form_class(request=request, instance=trp)
        formset = trip_formset(instance=trp)

    context = RequestContext(request)
    context['template_name'] = 'ctrip/trip_editor.html'

    context['form'] = form
    context['formset'] = formset
    context['slug'] = slug

    return render_to_response(context['template_name'],
                              {},
                              context_instance=context)
