from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import CadastroAdvogadoForm, LoginForm

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

def login(request):
    form = LoginForm()
    user = None
    if request.method == "POST":
        form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["email"]
        password = form.cleaned_data["senha"]
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index.html")
    else:
        form.add_error(None, "Invalid username or password")
        return render(request, "login.html", {"form": form})
