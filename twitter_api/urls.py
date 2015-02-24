from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'twitter_feed.views.home', name='home'),
    url(r'^twitter-ajax/$', 'twitter_feed.views.twitter_ajax', name='twitter_ajax'),
    url(r'^github-ajax/$', 'twitter_feed.views.github_ajax', name='github_ajax'),

    url(r'^admin/', include(admin.site.urls)),
)
