from django.urls import path
from .views import *

urlpatterns = [
    path('matutor/register', macreateView.as_view()),
    path('matutor/list',malistView.as_view()),
    path('matutor/userpro/<int:id>/',UserProfileView.as_view()),
    
    
 

]