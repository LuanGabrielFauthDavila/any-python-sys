#DEFAULTS
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#UTILS
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
from .utils import gen_uuid, verify_dict
#MODELS
from django.contrib.auth.models import User
#MODELS REST
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.get(email=email)
        user = authenticate(username=user.username, password=password)
        
        print(user)
        if user is not None and user.is_active:
            token = Token.objects.get(user=user)
            # token = None
            if token is not None:
                token.delete()
            token = Token.objects.create(user=user)
            return Response({
                "user": {
                    "email": user.email,
                    "name": user.get_username(),
                    "last_login": user.last_login,
                },
                "token": token.key
            }, status=201)
        return Response({ 'message': 'erro' })
    

def register(request):
    return Response({ 'message': 'ok' })