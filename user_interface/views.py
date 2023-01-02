from django.shortcuts import render, redirect
from django.contrib import messages
from user_auth.views import (
    create_user,
    login_user,
    list_users,
    personal_detail,
    get_profile,
    update_password,
)
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect("/list-users/1")

    message = ""
    if request.method == "POST":
        user_data = request.POST
        user_data = user_data.dict()

        name = user_data["first_name"] + " " + user_data["last_name"]
        email = user_data["email"]

        if user_data["password"] != user_data["confirm_password"]:
            messages.info(request, "Password and Confrim Password are not match.")
            return redirect("register")

        user_data_response = create_user(user_data)
        if user_data_response["success"]:
            email_data = {
                "email": email,
                "subject": "Welcome in the User Authentication",
                "name": name,
                "message": "Hi, {} welcome in the User Authentication.".format(name),
            }
            send_email(email_data)
            message = user_data_response["message"]
            messages.info(request, message)
            return render(request, "login.html")
        else:
            message = user_data_response["message"]
            messages.info(request, message)
            return render(request, "register.html")

    return render(request, "register.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("/list-users/1")

    message = ""
    if request.method == "POST":
        user_data = request.POST
        user_data = user_data.dict()

        if not user_data["password"]:
            messages.info(request, "Password should not be empty.")
            return redirect("login")

        user_data_response = login_user(request, user_data)
        if user_data_response["success"]:
            return redirect("/list-users/1")
        else:
            message = user_data_response["message"]
            messages.info(request, message)
            return render(request, "login.html")

    return render(request, "login.html")


def dashboard(request, page=1):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    current_user = request.user
    users_list = list_users(current_user.id, page)
    users_list_data = {"users": users_list["data"]}

    return render(request, "dashboard.html", users_list_data)


def profile(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    message = ""
    if request.method == "POST":
        current_user = request.user
        user_data = request.POST
        user_data = user_data.dict()
        user_data_response = personal_detail(current_user.id, user_data)
        message = user_data_response["message"]
        messages.info(request, message)
        return redirect("/accounts/profile/")
    else:
        current_user = request.user
        user_data_response = get_profile(current_user.id)
        user = {"user": user_data_response}
        return render(request, "profile.html", user)


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("login")

    message = ""
    if request.method == "POST":
        current_user = request.user
        user_data = request.POST
        user_data = user_data.dict()

        user_data_response = update_password(request, current_user.id, user_data)

        if user_data_response["success"]:
            name = current_user.first_name + " " + current_user.last_name
            email_data = {
                "email": current_user.email,
                "subject": "Password Updated",
                "name": name,
                "message": "Hi, {} your account password has been updated.".format(
                    name
                ),
            }
            send_email(email_data)
            message = user_data_response["message"]
            messages.info(request, message)
            return redirect("login")
        else:
            message = user_data_response["message"]
            messages.info(request, message)
            return render(request, "change-password.html")

    return render(request, "change-password.html")


def send_email(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
