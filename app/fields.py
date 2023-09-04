from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from random import choices

import string


def generate_id_string(prefix: str) -> str:
    return (
        f"{str(prefix)}_{''.join(choices(string.ascii_letters + string.digits, k=27))}"
    )


class IDField(models.CharField):
    def __init__(self, prefix="idn", *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault("primary_key", True)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("max_length", 32)
        kwargs.setdefault("verbose_name", _("id"))
        kwargs.setdefault("default", generate_id_string(prefix))
        super().__init__(*args, **kwargs)
