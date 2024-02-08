from django.shortcuts import render, redirect
from users.forms import UserCreationForm
from django.http import HttpResponse



def register_user_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("sucess-login")
    else:
        form = UserCreationForm()
    return render(request, "./registration/register.html", {"form": form})


def success_login(request):
    return HttpResponse("Succesful registration and authentication", content_type="text/plain")