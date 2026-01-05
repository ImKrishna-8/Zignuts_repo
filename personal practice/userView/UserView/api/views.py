from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.

class UserViewTest(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        
        return Response(serializer.data,status=200)
    
    def post(self,request):
        if User.objects.filter(username=request.data['username']).exists():
            return Response({"Error":"Already Exists"},status=400)
    
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        

class UserUpdateView(APIView):
    
    def get(self,request,id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=200)
    
    def put(self,request,id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
    
    def delete(self,request,id):
        user = User.objects.get(id=id)
        user.delete()
        return Response({"Message":"User Deleted"},status=204)

