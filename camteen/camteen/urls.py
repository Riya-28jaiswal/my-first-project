"""
URL configuration for camteen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
admin.site.site_header = "canteen Admin"
admin.site.site_title = "canteen Admin Portal"
admin.site.index_title = "Welcome to canteen management Portal"
from home.views import index,AboutUs, Menu, Features, Catering, ContactUs,  submit_contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('AboutUs/',AboutUs),
    path('Menu/',Menu),
    path('Features/',Features),
    path('Catering/',Catering),
    path('ContactUs/',ContactUs),
    path('submit_contact_view/', submit_contact_view, name='submit_contact_view'),
    # path('saveEnquiry/',saveEnquiry),
]
