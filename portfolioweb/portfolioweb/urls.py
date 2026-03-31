"""
URL configuration for portfolioweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from core import views as core_views
from portfolio import views as portfolio_views
from infoPersonal import views as info_views
from django.urls import path, include

from django.conf import settings


admin.site.site_header = "Administrador de SoftReady"
admin.site.site_title = "SoftReady Admin"
admin.site.index_title = "Panel de Administración"

urlpatterns = [
    path('', info_views.home, name = "home"),
    path('about-me/', info_views.about, name = "about"),
    path('portfolio/', portfolio_views.portfolio, name = "portfolio"),
    path('contact/', info_views.contact, name = "contact"),
    path('admin/', admin.site.urls),
     path("ckeditor5/", include("django_ckeditor_5.urls"))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

