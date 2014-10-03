from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from walkysite import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'walkysite.views.home', name='home'),
	url(r'^$', 'walkysite.views.index'),
	url(r'^jsdev/', include('jsdev.urls', namespace="jsdev")),
	#url(r'^jsdev/$', include('jsdev.urls', namespace="jsdev")),
	url(r'^maps_test/$', 'route.views.maps_test'),
	url(r'^maps/$', 'route.views.maps'),
	#url(r'^mapsdraw/$', 'route.views.mapsdraw'),
	#url(r'^updt/$', 'route.views.save_data'),
	url(r'^updt/$', 'route.views.update'),
	url(r'^cleardb/$', 'route.views.clearDB'),
	url(r'^all/$', include('route.urls')),
	#url(r'^map_from_db/$', 'route.views.show_map'),
	url(r'^map_from_db/$', 'route.views.get_points'),
	url(r'^places/$', 'route.views.places'),
	url(r'^routeList/$', 'route.views.routeList'),
    # url(r'^$', 'walkysite.views.home', name='home'),
    # url(r'^walkysite/', include('walkysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

#MEdia path for map_images
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
