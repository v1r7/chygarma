from django.contrib.auth import get_user_model

import re
User = get_user_model()


def authenticate(login, password):
    try:
        user = User.objects.get(login=login)
        print(user)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None


def create_user(data: dict):

    user = User(login=data.get('login'))
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.email = data.get('email')
    user.set_password(data.get('pass1'))

    user.save()

    return user


phone_number_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check_email(email):
    if re.search(phone_number_regex, email):
        return True
    return False