from multiprocessing import context
from django import shortcuts
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {
        "form":form
    }
    return render(request, "accounts/register.html", context=context)

# Create your views here.
def login_view(request):
    # if request.user.is_authenticated:
    #     return render(request, "accounts/already-logged-in.html", {})

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # # print(username, password)
        # user =  authenticate(request, username=username, password=password)
        # if user is None:
        #     context = {"error": "Inavlid username or password."}
        #     return render(request, "accounts/login.html", context)
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "accounts/login.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return render(request, "accounts/logout.html", {})

