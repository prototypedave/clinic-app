from django.contrib import admin
from django.urls import include, path
from oauth2_provider import urls as oauth2_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path('o/', include(oauth2_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)