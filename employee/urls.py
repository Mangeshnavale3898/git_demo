from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),  #new
    path('display/',views.display),
    path('insert/',views.insert),
    path('update/',views.update),
    path('delete/',views.delete),

]