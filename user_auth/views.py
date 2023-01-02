from datetime import datetime
from user_auth.models import User
from django.shortcuts import redirect
from user_auth.serializer import CreateUserSerializer
from helpers import params_validator, date_converter
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def create_user(params):
    required_parameters = [
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "email",
        "phone_number",
        "type",
        "password",
    ]

    # params_validator function checks for empty parameters in params - these params are defined in required_parameters list
    are_params_valid = params_validator(params, required_parameters)

    # checks if are_params_valid is True, it means the params are valid
    # checks if are_params_valid is False, it means the params are not valid
    if not are_params_valid:
        response = {
            "success": are_params_valid,
            "message": "One or more required parameters are missing.",
        }
        return response

    date_of_birth = params["date_of_birth"]

    # convert date_of_birth from string to date object and if date_of_birth empty string then convert into None
    date_of_birth = date_converter(date_of_birth)

    save_serializer_response = CreateUserSerializer(data=params)
    if save_serializer_response.is_valid():
        save_serializer_response.save()

        response = {"success": True, "message": "User created successfully."}
        return response
    else:
        response = {"success": False, "message": save_serializer_response.errors}
        return response


def login_user(request, params):
    email = params.get("email")
    phone_number = params.get("phone_number")
    password = params.get("password")

    if email:
        try:
            get_user = User.objects.get(email=email, is_deleted=False)
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                response = {
                    "success": True,
                    "message": "User logged in successfully.",
                }
                return response
        except User.DoesNotExist:
            response = {
                "success": False,
                "message": "User does not exist.",
            }
            return response

    if phone_number:
        try:
            get_user = User.objects.get(phone_number=phone_number, is_deleted=False)
            user = authenticate(email=get_user, password=password)
            if user:
                login(request, user)
                response = {
                    "success": True,
                    "message": "User logged in successfully.",
                }
                return response
        except User.DoesNotExist:
            response = {
                "success": False,
                "message": "User does not exist.",
            }
            return response

    response = {
        "success": False,
        "message": "You have logged in with another method.",
    }
    return response


def list_users(params, page):
    users = User.objects.filter(is_deleted=False).exclude(id=params)
    user_list_pagination = Paginator(users, 5)

    try:
        users = user_list_pagination.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page
        users = user_list_pagination.page(user_list_pagination.num_pages)

    response = {
        "success": True,
        "message": "Users list fetched successfully.",
        "data": users,
    }
    return response


def logout_user(request):
    logout(request)
    return redirect("login")


def personal_detail(user, params):
    required_parameters = [
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "email",
        "phone_number",
    ]

    # params_validator function checks for empty parameters in params - these params are defined in required_parameters list
    are_params_valid = params_validator(params, required_parameters)

    # checks if are_params_valid is True, it means the params are valid
    # checks if are_params_valid is False, it means the params are not valid
    if not are_params_valid:
        response = {
            "success": are_params_valid,
            "message": "One or more required parameters are missing.",
        }
        return response

    date_of_birth = params["date_of_birth"]

    # convert date_of_birth from string to date object and if date_of_birth empty string then convert into None
    date_of_birth = date_converter(date_of_birth)

    current_user = User.objects.filter(id=user, is_deleted=False).update(
        first_name=params["first_name"],
        last_name=params["last_name"],
        gender=params["gender"],
        date_of_birth=params["date_of_birth"],
        email=params["email"],
        phone_number=params["phone_number"],
        updated_date=datetime.now(),
    )

    if current_user:
        response = {"success": True, "message": "Profile updated successfully."}
        return response
    else:
        response = {"success": False, "message": current_user}
        return response


def get_profile(params):
    current_user = User.objects.get(id=params, is_deleted=False)
    return current_user


def update_password(request, user_id, params):
    required_parameters = [
        "old_password",
        "new_password",
        "new_conf_password",
    ]

    # params_validator function checks for empty parameters in params - these params are defined in required_parameters list
    are_params_valid = params_validator(params, required_parameters)

    # checks if are_params_valid is True, it means the params are valid
    # checks if are_params_valid is False, it means the params are not valid
    if not are_params_valid:
        response = {
            "success": are_params_valid,
            "message": "One or more required parameters are missing.",
        }
        return response

    current_password = params["old_password"]
    new_password = params["new_password"]

    user = User.objects.get(id=user_id, is_deleted=False)
    check = user.check_password(current_password)

    if check == True:
        user.set_password(new_password)
        user.save()
        User.objects.filter(id=user_id, is_deleted=False).update(
            updated_date=datetime.now()
        )

        logout(request)
        response = {"success": True, "message": "Password updated successfully."}
        return response
    else:
        response = {"success": False, "message": "Incorrect Current Password!!!"}
        return response
