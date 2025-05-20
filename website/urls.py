from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name="home"), # also act as login page    
   # path('login/' , views.login_user , name="login"),
    path('logout' , views.logout_user , name="logout"),  # name= "logout" This is the name used in templates
    path('register' , views.register_user , name="register"),
    path('record/<int:pk>' , views.customer_record , name="record"),  #localhost:800/record/2    2 is the id in the db
    path('delete_record/<int:pk>' , views.delete_customer , name="delete_customer"),
    path('add_record' , views.add_customer , name= "add_customer"),
    path('update_record/<int:pk>' , views.update_customer , name= "update_customer"),

]