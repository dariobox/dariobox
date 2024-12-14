from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dariobox/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('dariobox/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('dariobox/access/', include('access.urls')),
    path('dariobox/shipments/', include('shipments.urls')),
]
