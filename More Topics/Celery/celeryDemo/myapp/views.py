from django.shortcuts import render
from .tasks import add
from celery.result import AsyncResult
def index(request):
    result = add.delay(10,20)
    print(result)
    return render(request,'index.html',{'result':result})

def result(request,id):
    task = AsyncResult(id=id)
    print(task.ready())
    print(task.successful())
    print(task.failed())
    return render(request,'result.html',{'task':task})