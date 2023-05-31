from django.contrib import admin
from django.urls import path
from . import views
app_name='myapp'

urlpatterns = [
    path('',views.home,name=''),
    path('login/',views.login,name='login'),
    path('signup/',views.sign_up,name='signup'),
    path('user/<int:id>',views.user_account,name='user'),
    path('update/<int:id>',views.edit_profile,name='update'),
    path('change_pswd/<int:id>',views.Change_password,name='change_pswd'),
    path('logout/',views.logout,name='logout'),
    
    # ----------------gallery-------------------
    path('gal_home/',views.gallery,name='gal_home'),
    path('detailed/<int:id>',views.image_details,name='detailed'),
     
    
]
