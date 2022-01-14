from django.http.response import Http404
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import generics,mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import (
    LoginSerializer, RegisterSerializer, TokenSerializer)
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login,get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.conf import settings


User =get_user_model()


# when u get time read api guide generic views 

# token is only genrated for users not models


def create_auth_token(user):
    token1,_= Token.objects.get_or_create(user=user)
    #serializer=TokenSerializer(token1)
    #print(serializer.data)
    return token1.key


class LoginView(APIView):
    
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)      
        if serializer.is_valid():
             #python data type not json
            login(request, serializer.validated_data['user'])
            x=create_auth_token(serializer.validated_data['user'])
            return Response({'Token': x},status=status.HTTP_200_OK)
        else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegisterView(APIView):
    serializer_class_=RegisterSerializer
    def post(self, request,format=None):      
        ss = RegisterSerializer(data=request.POST)
        if ss.is_valid():
            ss.save()
            print(ss.instance)
            x=create_auth_token(ss.instance)    # need to explore
            return Response({'Token': x},status=status.HTTP_200_OK)
        else:
            return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)



'''
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )


    def retrieve(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''



