from django.urls import path
from django.conf.urls import url
from .import views
from .views import *
urlpatterns = [
   path('',views.indexx,name='indexx'),
   path('signup',views.signup,name='signup'),
   path('login1/',views.user_login,name='login1'),
   path('startt/',views.start_quiz,name='startt'),
   path('questions/',views.question_view,name='questions'),
   path('logout',views.logout,name='logout'),
   path('answers/',views.submit_quiz,name='answers'),
   path('error/',views.error,name='error'),
   path('check_answer/<int:user_id>',views.check_answer,name='check_answers'),
]