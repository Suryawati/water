from django.urls import path
from .views import HomePageView, DashboardView, UserProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('userprofile', UserProfileView.as_view(), name='page-user'),
]
