"""customerapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', views.customerListCreateAPIView.as_view(), name='api'),
    path('api/<int:pk>', views.customerRetrieveUpdateDestroyAPIView.as_view(), name='apid'),
    path('get-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
