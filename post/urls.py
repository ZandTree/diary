from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='list'),
    url(r'^create/$',views.CreatePost.as_view(),name='create'),
    url(r'^detail/(?P<pk>\d+)/$',views.DetailPost.as_view(),name='detail'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
    url(r'^edit/(?P<pk>\d+)/$',views.UpdatePost.as_view(),name='update'),
    url(r'^search/$',views.Search.as_view(),name='search'),


]
