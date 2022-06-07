from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('work/', views.work, name = 'work'),
    path('hello/<st_id>', views.hello, name = 'hello'),
    path('show/<st_id>', views.show, name = 'show'),
    path('delete/<st_id>', views.deleteStudent, name = "deleteStudent")
]   
