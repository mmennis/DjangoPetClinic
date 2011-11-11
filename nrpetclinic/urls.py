from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nrpetclinic.views.home', name='home'),
    # url(r'^nrpetclinic/', include('nrpetclinic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^petclinic/$', 'petclinic.views.index'),
    url(r'^petclinic/find_owners/$', 'petclinic.views.owners.find_owners'),
    url(r'^petclinic/owners/$', 'petclinic.views.all_owners'),
    url(r'^petclinic/owners/(?P<owner_id>\d+)$', 'petclinic.views.owners.owner'),
    
    url(r'petclinic/vets/$', 'petclinic.views.all_vets')
)
