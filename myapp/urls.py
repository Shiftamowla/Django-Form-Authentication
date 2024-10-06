from django.urls import path
from myapp.views import registerpage,loginpage,base,home

urlpatterns = [
    path('registerpage/', registerpage, name='registerpage'),
    path('loginpage/', loginpage,name='loginpage'),
    path('base/', base,name='base'),
    path('home/', home,name='home'),
]