from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path

urlpatterns = [
    path('', include('dresses.urls')),
    path('signup/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
    path('delivery/', views.flatpage, {'url': '/delivery/'}, name='delivery'),
    path('thank-you/', views.flatpage, {'url': '/thank-you/'}, name='thanks'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
