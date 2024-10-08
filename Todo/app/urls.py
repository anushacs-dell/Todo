from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('delete<int:id>',views.remove,name='remove_todo'),
    path('signup',views.register,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutpage,name='logout'),
    path('edit<int:id>',views.Edit,name='edits'),
    path('listing',views.List,name='listing'),
    path('calcu',views.Calcu,name='calculator')
]
