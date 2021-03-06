"""paint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views
from mysite.views import List, Detail , UserList, UserDetail , api_root
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$',views.add),
    url(r'^compare/$',views.compare),
      url(r'^pdf/$',views.pdf),
      url(r'^api/$',List.as_view()),
      url(r'^$',api_root),
      url(r'^user1/$',UserList.as_view()),
      url(r'^user2/$',UserDetail.as_view()),
      url(r'^api1/$',Detail.as_view()),
      url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
