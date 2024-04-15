from django.urls import path
from papergrading import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('papergradingclick', views.papergradingclick_view,name='papergradingclick'),
path('papergrade',views.papergrade,name='papergrade'),
path('paperresult/<str:filename>/',views.paperresult,name='paperresult')
]