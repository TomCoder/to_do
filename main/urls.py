from django.conf.urls.defaults import *
from main import views
urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        #url(r'^news/(?P<news_id>\d+)/$', views.news_view, name='news_view'),
)
