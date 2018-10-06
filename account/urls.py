from django.conf.urls import url
from django.urls import reverse_lazy
from account import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$',user_views.SignUp.as_view(),name='signup'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    url(r'^profile/$',user_views.ProfileView.as_view(),name='profile_view'),
    url(r'^update/profile/$',user_views.ProfileUpdate.as_view(),name='profile_update'),
    # urls for password change
    url(r'^change-password/$',user_views.MyPasswordChangeView.as_view(template_name='account/change-password.html'),
                name='change_password'),
    # urls for password reset

]
