from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import LoginSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
