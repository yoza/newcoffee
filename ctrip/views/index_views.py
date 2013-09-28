# site views here.
from django.template import RequestContext
from django.shortcuts import render_to_response


def index_view(request, slug='home'):
    """
    Index page view
    """
    context = RequestContext(request)


    context['slug'] = slug

    context['template_name'] = 'index.html'

    return render_to_response(context['template_name'],
                              {},
                              context_instance=context)
