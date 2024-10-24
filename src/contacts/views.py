from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.mixins import IPAccessMixin
from contacts.serializers import ContactSerializer
from contacts.models import Contact


class ContactViewSet(IPAccessMixin, ModelViewSet):

    permission_classes = [IsAuthenticated]

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(
            first_name__icontains=self.request.query_params.get('first_name', ''),
            last_name__icontains=self.request.query_params.get('last_name', ''),
        )
