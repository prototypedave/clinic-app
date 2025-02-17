from django.contrib import admin
from django.urls import include, path
from oauth2_provider import urls as oauth2_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path('o/', include(oauth2_urls)),
    path("appointments/", include("appointments.urls")),
    path("expense/", include("expense.urls")),
    path("medicine/", include("medicine.urls")),
    path("patient/", include("patients.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)