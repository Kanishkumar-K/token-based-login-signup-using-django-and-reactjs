from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name="token-obtain"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh-token"),
    path('register/', views.RegisterView.as_view(), name="register-user"),
    path('test/', views.protectedView, name="test"),
    path('dashboard/', views.dashboard, name="dashboard"),  #logged in
    path('', views.view_all_routes, name="all-routes"),
]
