
from django.urls import path, re_path
from Event import views

app_name='Event'
urlpatterns = [

    # Example: /Event/
    path('', views.LogLV.as_view(), name='index'),
#    path('<int:pk>/', views.LogDV.as_view(), name='detail'),

]
