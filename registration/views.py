from django.shortcuts import render,redirect,get_object_or_404,Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
#models
from django.contrib.auth import get_user_model
from .models import Profile
#forms
from .forms import CreateUserForm,ProfileUserForm
# forms and sessions (change password bu authenticated user)
from django.contrib.auth.forms import PasswordChangeForm

#for fbv from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView

User = get_user_model()


class SignUp(FormView):
    form_class = CreateUserForm
    # in this case niet nodig model = User
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('registration:login')

    # def dispatch(self,request,*args,**kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseForbidden()
        #return super().dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        User.objects.create_user(
            username = username,
            password = password
        )
        #Profile.objects.create(user=user)
        messages.success(self.request,'Account has been created!')
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin,DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'registration/profile.html'

    def get_object(self,queryset=None):
        obj = get_object_or_404 (
            Profile,
            user = self.request.user
        )
        if obj.user != self.request.user:
            raise Http404
        return obj


class ProfileUpdate(LoginRequiredMixin,UpdateView):
    form_class = ProfileUserForm
    model = Profile
    context_object_name = 'profile'
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('registration:profile_view')

    def get_object(self,queryset=None):
        return self.request.user.profile

    def form_valid(self,form):
        self.request.user.first_name = form.cleaned_data['first_name']
        self.request.user.last_name = form.cleaned_data['last_name']
        self.request.user.save()
        messages.success(self.request,'Account has been updated!')
        return super().form_valid(form)



class MyPasswordChangeView(PasswordChangeView):
    #docs built-in success_url = reverse_lazy('password_change_done')
    success_url = reverse_lazy('registration:profile_view')
    def form_valid(self,form):
        messages.success(self.request,'Password has been updated!')
        return super().form_valid(form)
