# WORKAROUND: https://code.djangoproject.com/ticket/24364 by reverting to default storage
from django.conf import settings, global_settings

settings.STATICFILES_STORAGE = global_settings.STATICFILES_STORAGE
