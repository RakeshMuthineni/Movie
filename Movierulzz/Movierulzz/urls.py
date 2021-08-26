"""Movierulzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Rating import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahesh/',views.info_view,name='mahesh'),
    path('htmlform/',views.htmlform_view,name='htmlform'),
    path('djangoform/',views.djangoform_view,name='djangoform'),
    path('modelform/',views.modelform_view,name='modelform'),
    path('delete/<int:id>',views.delete_view,name='delete'),
    path('delete_confirm/<int:id>',views.delete_confirm,name='delete_confirm'),
    path('updateform/<int:id>', views.update_view, name='updateform'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
