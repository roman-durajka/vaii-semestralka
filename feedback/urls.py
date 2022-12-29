from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('submit/', views.submit_idea, name="submit_idea"),
    path('results/', views.results, name="results"),
    path('results/paginate/', views.paginate, name="paginate"),
]
