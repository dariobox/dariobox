# example/urls.py
from django.urls import path

from example.views import ProtectedView


urlpatterns = [
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
]
