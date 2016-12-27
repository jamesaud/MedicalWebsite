# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from medweb.homepage import views as homepage_views

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # Your stuff: custom urls includes go here
    url(r'^$', homepage_views.index, name='home'),
    url(r'^test/$', homepage_views.test, name='test'),
    url(r'^about/$', homepage_views.about, name='about'),
    url(r'^create/$', homepage_views.create, name='create'),
    url(r'^invest/$', homepage_views.invest, name='invest'),
    url(r'^compare/$', homepage_views.compare, name='compare'),    
    url(r'^submit_newsletter/$', homepage_views.submit_newsletter, name='submit_newsletter'),
    url(r'^robots.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
