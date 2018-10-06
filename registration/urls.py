from django.conf.urls import url
from django.urls import reverse_lazy
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
    url(r'^password_reset/$',auth_views.PasswordResetView.as_view(
                success_url=reverse_lazy('registration:password_reset_done'),
                email_template_name='registration/password_reset_email.html',
                #subject_template_name='registration/password_reset_subject.txt'

                ),
                name='password_reset'),
    url(r'^password_reset/done/$',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
        success_url = reverse_lazy('registration:password_reset_complete')),
        # template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),



]
#
# url(r'^password_reset/$',
#             auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
#             name='password_reset'),
# url(r'^password_reset/done/$',
#             auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
#             name='password_reset_done'),
# url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#     auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
# url(r'^reset/complete/$',
#             auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
#             name='password_reset_complete'),
