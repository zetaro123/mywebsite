"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^arun/', views.index, name='index'),
    url(r'^register/',views.UserFormView.as_view(),name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^addpdt/',views.addproduct,name='addproduct'),
    url(r'^product/',views.showproduct,name='showproduct'),

    url(r'^admin/add',views.productadd,name='productadd')
    #url(r'^logout/$', logout, {'template_name': 'home/logout.html'}),
]