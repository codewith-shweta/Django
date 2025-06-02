from django.urls import path 
from . import views 

# localhost:8000/app
# localhost:8000/app/order
urlpatterns = [
    path('', views.all_template, name='all_template'),
    path('<int:app_id>/', views.all_desc, name='description')

]
