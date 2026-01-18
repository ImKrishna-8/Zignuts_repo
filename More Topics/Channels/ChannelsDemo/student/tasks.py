from .models import Student
from faker import Faker
from celery import shared_task
from .models import Student
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
fake = Faker()

@shared_task
def createStudent(no):
    channel_layer = get_channel_layer()
    for i in range(0,no):
        name = fake.name()
        surname = fake.last_name()
        address = fake.address()
        print(i)
        print("Im in taskkkkk")
        student = Student(name=name,surname=surname,address=address)
        async_to_sync(channel_layer.group_send)(
            "testgroup",{
                'type':'send_student',
                "data": {
                    "name": student.name,
                    "surname": student.surname,
                    "address": student.address,
                    "index": i + 1
                }
            }
        )
        
        

        
