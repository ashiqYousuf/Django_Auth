from blog import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name="home"),
    path('about/',views.about , name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('login/',views.user_login,name="login"),
    path('signup/',views.user_signup,name="signup"),
    path('logout/',views.user_logout,name="logout"),
    path('dashboard/addpost/',views.addpost,name="addpost"),
    path('dashboard/updatepost/<int:id>/',views.updatepost,name="updatepost"),
    path('dashboard/deletepost/<int:id>/',views.deletepost,name="deletepost"),
]
