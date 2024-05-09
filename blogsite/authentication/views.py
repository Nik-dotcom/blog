from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from .form import RegistartionForm
from django.contrib import messages
# Create your views here.

class Registration(View):
    def post(self, request):
        if request.method == 'POST':
            form = RegistartionForm(request.POST)
            if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Создан аккаунт {username}!')
                    return redirect('/')
            else:
                return render(request, 'users/register.html', {'form': form})
    
    def get(self, request):
        form = RegistartionForm()
        return render(request, 'users/register.html', {'form': form})
            
    