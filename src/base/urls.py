from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/data/', include('data.urls')),
    path('admin/', admin.site.urls),
]
