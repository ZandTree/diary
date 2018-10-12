from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120,empty_value='subject')
    email = forms.EmailField(help_text="should contain a @ sign")
    verify_email = forms.EmailField(help_text="please verify your email address")
    msg = forms.CharField(label="Your feedback message",
                    max_length=400,
                    widget=forms.Textarea(attrs={'rows':10,'cols':80}),
                    help_text = "Should be less than 400 characters")
    honey_pot = forms.CharField(required=False,
                    widget=forms.HiddenInput,
                    label='leave empty',
                    validators=[validators.MaxLengthValidator(0)],
                    )
