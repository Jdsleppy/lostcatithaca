from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import debug_toolbar


urlpatterns = [
    path("administration/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include("lostcats.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
