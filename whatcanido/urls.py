from django.urls import path
from . import views
app_name = 'whatcanido'

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name="donate"),
    path('contribute/', views.contribute, name="contribute"),
    path('problems/<slug:category_slug>/', views.problemlist, name='problem_list_category'),
    path('problems/', views.problemlist, name="problem_list_search"),
    path('problem/<slug:problem_slug>/', views.problem, name='problempage'),
    path('submitted/',views.submitted, name="submitted"),

]