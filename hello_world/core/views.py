from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

def login(request):
    return render(
        request,
        "login.html",
        {
            "title": "Login",
        },
    )

def faq(request):
    return render(
        request,
        "faq.html",
        {
            "title": "FAQ",
        },
    )