from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerSplitView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # Reemplazado por el LoginView
    TokenRefreshView,
)
from autenticacion.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # API's pequeñas. 
    path('api/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/split/', SpectacularSwaggerSplitView.as_view(), name='split'), # API's grandes. 
    path('almacen/', include('almacen.urls')),
    path('auth/token', LoginView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view(),)
]
