from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class UserView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=200)
    
class DetailUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        seralizer = UserSerializer(user)
        return Response(seralizer.data,status=200)
        
