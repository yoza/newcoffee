# -*- coding: UTF-8 -*-
"""
site extended settings
"""

SERVER_EMAIL = 'system@oleg.prans.net'
DEFAULT_FROM_EMAIL = 'noreply@oleg.prans.net'

APP_LABEL = "ctrip"

#'''
# settings for admin
#'''

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    'django.contrib.messages.context_processors.messages',
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
)

# ''' end '''
