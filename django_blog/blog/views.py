from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'blog/profile.html', {'user': request.user})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/edit_profile.html', {'user': request.user})
