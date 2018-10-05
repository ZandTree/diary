from django.conf.urls import url,include
from django.contrib import admin
# for static in debug
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registration/',include('registration.urls',namespace='registration')),
    #url(r'^registration/',include('django.contrib.auth.urls')),
    url(r'^$',TemplateView.as_view(template_name='_layout/home.html'),name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
