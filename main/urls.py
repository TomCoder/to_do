from django.conf.urls.defaults import *
from main import views
urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^list/$', views.to_dos, name='to_dos'),
        #url(r'^news/(?P<news_id>\d+)/$', views.news_view, name='news_view'),
        #url(r'^about/$', views.about, name='about'),
        #url(r'^contact/$', views.contact, name='contact'),
)
