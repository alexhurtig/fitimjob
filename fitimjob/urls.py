from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls), name="admin"),
                       url(r'^admin/dashboard', 'fitapp.views.dashboard', name="dashboard"),
                       url(r'^$', 'fitapp.views.fitHome', name="FIT-IM-JOB"),
                       url(r'^kontakt', 'fitapp.views.contact'),
                       url(r'^impressum', 'fitapp.views.impress'),
                       url(r'^live-bereich', 'fitapp.views.liveworkout'),
                       url(r'^login', 'fitapp.views.login'),
                       url(r'^logout', 'fitapp.views.logout'),
                       url(r'^news', 'fitapp.views.news'),
                       url(r'^registrieren', 'fitapp.views.register'),
                       url(r'^videos', 'fitapp.views.videoworkout'),
                       url(r'^team', 'fitapp.views.team'),
                       url(r'^maenner', 'fitapp.views.men'),
                       url(r'^anamnese', 'fitapp.views.anamnese'),
                       url(r'^frauen', 'fitapp.views.women'),
                       url(r'^unternehmen', 'fitapp.views.company'),
                       url(r'^personal-coaching', 'fitapp.views.coaching'),
                       url(r'^10-wochen-programm', 'fitapp.views.programm'),
                       url(r'^seminare', 'fitapp.views.seminar'),
                       url(r'^preise', 'fitapp.views.pricing'),
                       url(r'^agb', 'fitapp.views.agb'),
                       url(r'^add_form_data/$', 'fitapp.views.add_form_data')
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
