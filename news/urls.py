from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'), #d -> digit/ number w -> word
	url(r'^panel/news/list/$', views.news_list, name='news_list'),
	url(r'^panel/news/add/$', views.news_add, name='news_add'),
	url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
	url(r'^markdownx/', include('markdownx.urls')),
]

# url(r'^news/(?P<word>\w+)/$', views.news_detail, name='news_detail') #d -> digit/ number w -> word