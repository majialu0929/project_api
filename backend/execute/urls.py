
from django.urls import re_path
from execute import views


# execute/


urlpatterns = [
    re_path('debug/', views.execute_views),
    re_path('httpapi/', views.httpapi_views),

]