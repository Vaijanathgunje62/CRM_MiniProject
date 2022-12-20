from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from account.forms import NewUserForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views import View


class SignUpView(FormView):
    form_class = NewUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('account:homepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            return super().form_valid(form)

class Login(View):
    def get(self,*args):
            form = AuthenticationForm()
            return render(self.request, 'account/login.html',{'login_form':form })

    def post(self,request,*args):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
            form = AuthenticationForm()
            return render(request=request, template_name="account/login.html", context={"login_form":form})

