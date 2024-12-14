from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example.urls')), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refrescar token
]
