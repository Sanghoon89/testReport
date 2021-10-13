
from django.urls import path, re_path
from Event import views

app_name='Event'
urlpatterns = [

    # Example: /Event/
    path('', views.LogLV.as_view(), name='index'),

    # Example: /Event/archive/
    path('archive/', views.LogAV.as_view(), name='log_archive'),

    # Example: /Event/archive/2021/
    path('archive/<int:year>/', views.LogYAV.as_view(), name='log_year_archive'),

    # Example: /Event/archive/2021/aug/
    path('archive/<int:year>/<str:month>/', views.LogMAV.as_view(), name='log_month_archive'),

    # Example: /Event/archive/2021/aug/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.LogDAV.as_view(), name='log_day_archive'),

    # Example: /Event/archive/today/
    path('archive/today/', views.LogTAV.as_view(), name='log_today_archive'),

]
