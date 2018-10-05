from django.conf.urls import url

from registration import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$',user_views.SignUp.as_view(),name='signup'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    url(r'^profile/$',user_views.ProfileView.as_view(),name='profile_view'),
    url(r'^update/profile/$',user_views.ProfileUpdate.as_view(),name='profile_update'),
    url(r'^change-password/$',user_views.MyPasswordChangeView.as_view(template_name='registration/change-password.html'),
                name='change_password'),
    # url(r'^password-reset/$',
    #             auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
    #             name='reset_password'),
    # url(r'^password-reset/done/$',
    #             auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    #             name='reset_password_done'),
    # url(r'^password-reset-confirm/<uidb64>/<token>/$',
    #             auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    #             name='reset_password_confirm'),

]
