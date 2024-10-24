from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

import re


def validate_phone_number(value):
    if not re.match(r"^\+\d+$", value):
        raise ValidationError(
            _('Invalid phone number format. Example: +380501734729'),
        )
