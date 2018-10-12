from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='account:login')
def feedback(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['msg'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['nobody@gmail.com']
            )
            messages.success(request,'Thank you for your feedback')
            return HttpResponseRedirect(reverse('home'))

    return render(request,'suggestion/feedback.html',{'form':form})
