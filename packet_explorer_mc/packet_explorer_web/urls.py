from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'game.views.home', name='home'),
     url(r'^populate$', 'game.views.populate_db', name='populate'),
     url(r'^questions$', 'game.views.populate_questions', name='populate'),
     url(r'^question$', 'game.views.question', name='populate'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'packet_explorer_web.views.home', name='home'),
)
