from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import jdatetime
import datetime
import random
from django.utils import timezone

#handmade
from accounts.forms import UserForm
from commonuser.forms import CommonUserForm


def CommonUserSignupView(request):

    now = datetime.datetime.now()
    if request.method == 'POST':

            user_form = UserForm(data = request.POST)
            commonuser_form = CommonUserForm(data = request.POST)

            if user_form.is_valid() and commonuser_form.is_valid():
                 phone_number = commonuser_form.cleaned_data.get('phone_number')


                 user = user_form.save(commit=False)
                 user.is_commonuser = True
                 user.is_active = False
                 user.save()

                 request.session['user_slug'] =  user.slug
                 commonuser = commonuser_form.save(commit=False)
                 commonuser.user = user
                 if 'picture' in request.FILES:
                    commonuser.picture = request.FILES['picture']
                 commonuser.save()
                 
                 return HttpResponseRedirect(reverse('commonuser:confirmation'))
            else:
                # One of the forms was invalid if this else gets called.
                #redirect to another page or anything else
                print(user_form.errors,commonuser_form.errors)


    else:
            user_form = UserForm()
            commonuser_form = CommonUserForm()

            return render(request,'commonuser/commonusersignup.html',
                              {'user_form':user_form,
                               'commonuser_form':commonuser_form})
