from django.http import HttpResponseForbidden
from django.utils.translation import gettext as _

import ipapi


class IPAccessMixin:
    allowed_countries = ["UA", "PL"]

    def dispatch(self, request, *args, **kwargs):
        request_ip = request.META.get(request.META.get('REMOTE_ADDR'))
        country = ipapi.location(request_ip, output='country')

        if country not in self.allowed_countries:
            return HttpResponseForbidden(_("Access denied"))

        return super().dispatch(request, *args, **kwargs)
