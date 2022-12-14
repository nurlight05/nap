from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import showText

urlpatterns = [
    path('', include('landing.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path(r'competition/', showText, name="show_text")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
