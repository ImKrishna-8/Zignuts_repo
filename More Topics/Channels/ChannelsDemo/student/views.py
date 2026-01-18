from django.shortcuts import render
from .tasks import createStudent
# Create your views here.

def index(request):
    no = request.GET.get('no')
    result = createStudent.delay(int(no))
    return render(request,'index.html')