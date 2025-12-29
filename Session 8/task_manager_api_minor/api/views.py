from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Todo
from rest_framework.response import Response
from .serializers import TodoSerializer,UserSerializer
# Create your views here.

class UserView(APIView):
    permission_class=[AllowAny]

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({"error:",'User Already Exists'})
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data,status=201)


class TodoView(APIView):
    permission_classes=[IsAuthenticated]

    def get_object(self,id,user):
        return get_object_or_404(Todo,id=id,user=user)

    def get(self,request):
        tasks = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(tasks,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    def put(self,request,id):
        task = self.get_object(id,request.user)
        serializer = TodoSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=200)
        return Response(serializer.error,status=400)
    
    def delete(self,request,id):
        task = self.get_object(id,request.user)
        task.delete()
        return Response({"Message:":"Task Deleted Succesfully"},status=204)