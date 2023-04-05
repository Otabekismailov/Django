from django.urls import path
from polls.views import homepage, questions_list, questions_detile, vote, HomeListVies, question_add

app_name = 'polls'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_list, name='questions_list'),
    path('questions/<int:pk>/', questions_detile, name='questions_detile'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('list_of_questions/', HomeListVies.as_view(), name=
    'list_of_questions'),
    path('questions/add/', question_add, name='question_add'),
]

