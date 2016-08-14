from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pokemon$', 'search.views.index', name = 'index'),
    url(r'^random$', 'search.views.random', name = 'random'),
    url(r'^search$', 'search.views.srch', name = 'search'),
    url(r'^search/([0-9]+)', 'search.views.srch2', name = 'search'),
    url(r'^search/(?P<foo>[0-9]+)', 'search.views.srch2', name = 'search2'),
)