"""
simple site header
"""
from os.path import join
import re
from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag(takes_context=True)
def metadata_tag(context):
    """
    metadatA tag
    """
    metadata = ''
    title = 'Coffee trips'

    metadata += '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
    metadata += '<title>%s</title>' % title

    if 'keywords' in context:
        keywords = "%s" % (context['keywords'])
        metadata += '<meta name="keywords" content="%s" />' % keywords
    metadata += '<meta name="robots" content="follow, all" />'
    metadata += '<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
    app_label = getattr(settings, 'APP_LABEL', '')
    css_path = join(settings.STATIC_URL, app_label) + '/css/'
    if settings.DEBUG:
        js_suf = 'js'
    else:
        js_suf = 'min.js'
    js_path = join(settings.STATIC_URL, app_label) + '/js/'

    metadata += '<link rel="stylesheet" type="text/css" href="%sscreen.css" title="screen" media="screen"/>' % css_path

    metadata += '<script type="text/javascript" src="%s%s/js/jquery.min.js"></script>' % (settings.STATIC_URL, app_label)

    metadata += '<script type="text/javascript" src="%sbase.%s" charset="utf-8"></script>' % (js_path, js_suf)

    metadata += '<link rel="shortcut icon" href="%sfavicon.ico" type="image/x-icon"/>' % settings.STATIC_URL

    metadata += '<link rel="apple-touch-icon" href="%sapple_icon.png"/>' % settings.STATIC_URL

    return metadata
