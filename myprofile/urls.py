from django.urls import path
from .views import (
    MyProfileView, UserDetailView, CompanyDetailView, SubscriptionDetailView, UserUpdateView
)

app_name = "myprofile"

urlpatterns = [
    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
    path('<int:pk>/user_detail/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/user_update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/company_detail/', CompanyDetailView.as_view(), name='company-detail'),
    path('<int:pk>/subscription_detail/', SubscriptionDetailView.as_view(), name='subscription-detail'),
]
