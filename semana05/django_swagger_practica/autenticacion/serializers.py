from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user) #Recuperamos la token.
        token['username'] = user.username
        token['email'] = user.email
        return token