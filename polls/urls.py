from django.urls import path
from polls.views import homepage, questions_list, questions_detile, vote, results

app_name = 'polls'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_list, name='questions_list'),
    path('questions/<int:pk>/', questions_detile, name='questions_detile'),
    path('<int:question_id>/vote/', vote, name='vote'),
    # path('<int:question_id>/results/', results, name='results'),
]
