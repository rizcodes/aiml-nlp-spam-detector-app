from django.urls import path
from app_spam_detector.views import CheckSpamView

urlpatterns = [
    path('checkSpam/', CheckSpamView.as_view(), name='checkSpame'),
]
