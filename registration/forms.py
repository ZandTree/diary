from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.core import validators

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
def must_be_empty(value):
    if value:
        raise forms.ValidationError('should be empty')

class CreateUserForm(UserCreationForm):
    # label in this syntax is invisable in developer tools because of hidden widget but can be visable
    honey_pot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label='leave me',
        #validators = [validators.MaxLengthValidator(0)]
        validators = [must_be_empty]
        )
    username = forms.CharField(
                        max_length=120,
                        validators=[validators.RegexValidator(regex = USERNAME_REGEX,message='Without @ sign'),validators.MinLengthValidator(2)],
                        # code='invalid sign in username'
                        )
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        # honey_pot must be mentioned otherwise it wouldn't be in a form for evaluation
        fields =['username','email','password1','password2','honey_pot']
        model = User




    # when to use this (.save())?
    # def save(self,commit=True):
    #     # first = call for parent eval, but NOT commit
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data.get('email') # let op this field is NOT REQUIRED!
    #     # the same could be applied for the others
    #     if commit:
    #         # here call for own .save()
    #         user.save()
    #     return user


class ProfileUserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        fields = ['first_name','last_name', 'avatar','age','location','bio']
        model = Profile
