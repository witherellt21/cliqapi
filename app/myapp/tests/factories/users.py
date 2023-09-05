import factory
from faker import Faker

from ...models import User

fake = Faker()


def random_username(user):
    return user.simple_profile.get("username")


def random_first_name(user):
    return user.simple_profile.get("name").split(" ", -1)[0]


def random_last_name(user):
    return user.simple_profile.get("name").split(" ", -1)[1]


class UserFactory(factory.django.DjangoModelFactory):
    simple_profile = factory.LazyFunction(fake.simple_profile)

    first_name = factory.LazyAttribute(lambda o: random_first_name(o))
    last_name = factory.LazyAttribute(lambda o: random_last_name(o))
    email = factory.LazyFunction(fake.email)
    username = factory.LazyAttribute(lambda o: random_username(o))
    is_staff = False
    is_active = True

    class Meta:
        model = User
        exclude = ("simple_profile",)
