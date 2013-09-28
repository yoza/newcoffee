"""
coffetrip urls
"""

from django.conf.urls import patterns, include, url

from django.contrib import admin
from ctrip.views import index_view
from ctrip.views.trip_views import trip_view, delete_trip_view


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^trip/(?:(?P<slug>[-\w.]+)/)?(/)?$', trip_view, name='trip-view'),

    url(r'^delete-trip/$', delete_trip_view, name='delete-trip'),

    url(r'^(?:(?P<slug>home)/)?$', index_view, name='pages-root'),
)
