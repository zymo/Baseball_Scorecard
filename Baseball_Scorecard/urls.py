from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Baseball_Scorecard.views.home', name='home'),
    # url(r'^Baseball_Scorecard/', include('Baseball_Scorecard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'scorecard.views.welcome'),    
    url(r'^add_player/$', 'scorecard.views.add_player'),
    url(r'^new_game/$', 'scorecard.views.new_game'),
    url(r'^current_game/$', 'scorecard.views.current_game'),
    url(r'^add_lineups/$', 'scorecard.views.add_lineups'),
)
