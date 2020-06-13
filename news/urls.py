from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail') #d -> digit/ number w -> word
]

# url(r'^news/(?P<word>\w+)/$', views.news_detail, name='news_detail') #d -> digit/ number w -> word