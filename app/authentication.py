from django.contrib.auth import get_user_model

from django.contrib.auth.backends import ModelBackend


UserModel = get_user_model()


class EmailAuthBackend(ModelBackend):
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        #     try:
        #         user = User.objects.get(email=username)
        #         if user.check_password(password):
        #             return user
        #         return None
        #     except User.DoesNotExist:
        #         return None

        # print(UserModel.USERNAME_FIELD)
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            # print("checking password")
            # print(user.email)
            # print(user.password)
            # print(password)
            # print(user.check_password(str(password)))
            # print(self.user_can_authenticate(user))
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


# def get_user(self, user_id):
#     try:
#         return UserModel.objects.get(pk=user_id)
#     except UserModel.DoesNotExist:
#         return None
