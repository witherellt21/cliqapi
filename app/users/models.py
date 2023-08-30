from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, AbstractUser

# from django.contrib.auth.models
from django.core.mail import send_mail

from .managers import UserManager


# class User(models.Model):
#     """Base model for a users profile."""

#     username = models.CharField(_("Username"), primary_key=True, max_length=40)
#     email_address = models.EmailField(_("Email Address"), unique=True)
#     first_name = models.CharField(_("First Name"), max_length=50, default="", null=True)
#     last_name = models.CharField(_("Last Name"), max_length=50, default="", null=True)
#     date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
#     avatar = models.ImageField(_("Avatar"), upload_to="avatars/", null=True, blank=True)
#     external_id = models.CharField(_("external_id"), unique=True)

#     REQUIRED_FIELDS = ("username", "external_id")
#     USERNAME_FIELD = "username"

#     class Meta:
#         verbose_name = _("user")
#         verbose_name_plural = _("users")

#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = "%s %s" % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         """
#         Returns the short name for the user.
#         """
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """
#         Sends an email to this User.
#         """
#         send_mail(subject, message, from_email, [self.email], **kwargs)


class User(AbstractUser, PermissionsMixin):
    """Base auth user model that overrides the django auth user model."""

    id = models.CharField(primary_key=True, max_length=40)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    email_address = models.EmailField(_("email address"))

    objects = UserManager()

    # EMAIL_FIELD = "email"
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
