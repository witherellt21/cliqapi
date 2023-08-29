from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, m2m_changed, pre_save

# from .models import User, Profile


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, **kwargs):
#     if not hasattr(instance, "profile") or instance.profile == None:
#         profile = Profile.objects.create(user=instance)
