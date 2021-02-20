from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print(f"VALID")
            form.save()
        else:
            print("NOT VALID")
        return HttpResponseRedirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
