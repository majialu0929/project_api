from django.urls import re_path
from . import views
from django.urls import re_path

from . import views

# execute/


urlpatterns = [
    re_path('debug/', views.execute_views),
    re_path('ceshi/', views.ceshi_views),

]