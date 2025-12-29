from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer,TaskSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404 
from .models import Task
# Create your views here.

class UserView(APIView):
    permission_classes=[AllowAny]

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):

        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({"error:": "User already Exists"},status=400)
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data,status=201)
    
 
class TaskView(APIView):

    permission_classes=[IsAuthenticated]
    
    def get_object(self, id, user):
        return get_object_or_404(Task, id=id, user=user) 

    def get(self, request):
        status = request.GET.get('status')
        tasks = Task.objects.filter(user=request.user)

        if status:
            tasks = tasks.filter(status=status)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

    def put(self, request, id):
        task = self.get_object(id=id, user=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
    
    def delete(self,request,id):
        task = self.get_object(id=id,user=request.user)
        task.delete()
        return Response({"message":"Task Deleted Succesfully"},status=204)
