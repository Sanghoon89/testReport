from django.urls import path, re_path
from Remote import views

app_name='Remote'
urlpatterns = [

    # Example: /Remote/
    path('', views.KeepLV.as_view(), name='index'),

]
