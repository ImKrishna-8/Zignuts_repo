from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('checkout/',views.checkout),
    path('orders/<order_id>',views.orderDetail,name='order_detail'),
    path('orders/',views.orders,name='orders_list'),
    path('signup',views.signup),
    path('login',views.loginHandler),
    path('logout/',views.logoutHandler),
    path('about/',views.about,name='about'),
    path('conmtact/',views.contact,name='contact'),
]