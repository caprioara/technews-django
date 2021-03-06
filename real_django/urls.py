from django.conf.urls import include, url
from django.contrib import admin

#for photos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
    url(r'', include('news.urls')),
    url(r'', include('cat.urls')),
    url(r'', include('subcat.urls')),
]

if settings.DEBUG:

	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
