from django.conf.urls import url,include
from django.contrib import admin
# for static in debug
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from suggestion.views import feedback

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^suggestion/$',feedback,name='feedback'),
    url(r'^account/',include('account.urls',namespace='account')),
    url(r'^account/',include('django.contrib.auth.urls')),
    url(r'^$',TemplateView.as_view(template_name='_layout/home.html'),name='home'),
    url(r'^post/',include('post.urls',namespace='post')),
    #url(r'^suggestion/$',feedback,name='feedback'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
