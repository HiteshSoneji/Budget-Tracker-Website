from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/home/', views.home, name='home'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name = 'login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/home_graph/', views.graph_view, name='graph'),
    path('accounts/home_expenses/', views.expense_view, name='expenses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
]