from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages
# Create your views here.

def registerUser(request):
  if request.method == 'POST':
    print(request.POST)
    form = UserForm(request.POST)
    if form.is_valid():
      password = form.cleaned_data['password']
      user = form.save(commit=False)
      user.set_password(password)
      user.role = User.CUSTOMER
      user.save()
      messages.error(request, 'Your account has been registered successfully !')
      return redirect('registerUser')
    else:
      print('Invalid form')
      print(form.errors)
  else:
    form = UserForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/registerUser.html', context)