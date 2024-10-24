from django.urls.conf import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet

app_name = 'contacts'

router = routers.DefaultRouter()
router.register('contacts', ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
