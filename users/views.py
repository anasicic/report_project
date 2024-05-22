from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegisterForm




def register(request):
	if request.method =="POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'Your account has been created! You are now able to log in')
			login(request, user)
			return redirect('invoice-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Promijeni "profile" s pravim URL-om za prikaz profila
    else:
        form = UserRegisterForm(instance=user)
    return render(request, 'users/profile.html', {'form': form})






