from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('Echango.urls')),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', include('pwa.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
