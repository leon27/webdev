from django.conf.urls import patterns, include, url

from django.contrib import admin
from MyApp.views import index,sum
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JSONDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'sum',sum),
)
