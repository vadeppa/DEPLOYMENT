"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ojas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('sigup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_loguot,name='logout'),
    path('contact/',views.Contact,name='contact'),
    path('fee',views.feedback,name='feed'),
    path('dash/',views.dashborad,name='dashboard'),
    # path('edit/<int:id>',views.edite,name='edit'),
    # path('delete/<int:id>',views.delet,name='delete'),
    path('delete/<int:id>/', views.DeleteView.as_view(), name='delete'),
    path('edit/<int:id>/', views.EditView.as_view(), name='edit'),
    path('set/',views.set_cookie),
    path('get/',views.get_cookie),
    path('del/',views.del_cookie),
    path('set1/',views.set_session),
    path('get2/',views.get_session),
    path('del2/',views.del_session),
]
