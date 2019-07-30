from django.contrib import admin
from django.urls import path, include
import wedblog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wedblog.views.home, name="home"),
    path('wedblog/', include('wedblog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('wedblog/<int:wedblog_id>/', wedblog.views.detail, name="detail"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)