from django.urls import path
from .views import GoogleLogin, SendOTP, VerifyOTP,RegisterView

urlpatterns = [
    path('auth/google/', GoogleLogin.as_view(), name='google-login'),
    path('auth/send-otp/', SendOTP.as_view(), name='send-otp'),
    path('auth/verify-otp/', VerifyOTP.as_view(), name='verify-otp'),
    path('register/', RegisterView.as_view(), name='register'),
    
]
