"""blog URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from rest_framework import routers

from blogpost import views

from blogpost.PageSitemap import PageSitemap
from blogpost.FlatPageSitemap import FlatPageSitemap
from blogpost.BlogSitemap import BlogSitemap
from blogpost import BlogpostSet

sitemaps = {
    'page': PageSitemap,
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
}

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostSet, 'blogpost-list')


urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^blog/(?P<slug>.+).html', views.view_post, name='blog_post'),
    url(r'^admin/', admin.site.urls),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(apiRouter.urls)),
]
