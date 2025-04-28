"""mppDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from mppDemoApp.views import index,Gallery,AboutUs,AboutCollege,AboutPrincipal,AboutBranch,AboutLibrary,Facilities,Faculty,Registration,ContactUs,Login,\
    SDashboard,feedback,Schangepassword,Myprofile,logout,Adashboard,ViewEnquiry,ViewFeedback,\
    Changepassword,ViewRegistration,Rdelete,Rupdate,alogout,Aupdate,AddNotification,Adelete,ViewNotification,ANdelete,captcha
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('index/',index),
    path('Gallery/',Gallery),
    path('AboutUs/', AboutUs),
    path('AboutCollege/',AboutCollege),
    path('AboutPrincipal/',AboutPrincipal),
    path('AboutBranch/', AboutBranch),
    path('AboutLibrary/',AboutLibrary),
    path('Facilities/',Facilities),
    path('Faculty/',Faculty),
    path('Registration/',Registration),
    path('ContactUs/',ContactUs),
    path('Login/',Login),
    path('UserZone/SDashboard/',SDashboard),
    path('UserZone/feedback/',feedback),
    path('UserZone/schangepassword/',Schangepassword),
    path('UserZone/myprofile/',Myprofile),
    path('UserZone/logout/',logout),
    path('AdminZone/Adashboard/',Adashboard),
    path('AdminZone/ViewEnquiry/',ViewEnquiry),
    path('AdminZone/ViewFeedback/',ViewFeedback),
    path('AdminZone/Changepassword/',Changepassword),
    path('AdminZone/ViewRetration/',ViewRegistration),
    path('AdminZone/Rdelete/',Rdelete),
    path('AdminZone/Rupdate/',Rupdate),
    path('AdminZone/alogout/',alogout),
    path('AdminZone/Adelete/',Adelete),
    path('AdminZone/Aupdate/', Aupdate),
    path('AdminZone/AddNotification/',AddNotification),
    path('AdminZone/ViewNotification/', ViewNotification),
    path('AdminZone/ANdelete/',ANdelete),
    path('captcha/',captcha),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
