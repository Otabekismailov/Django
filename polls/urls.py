from django.urls import path
from polls.views import hopage

urlpatterns = [
    path('', hopage),
]
