from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add_entry/', views.add_entry, name="add_entry"),
    path('history_list/', views.history_list, name="history_list"),
    path('delete_entries/', views.delete_entries, name="delete_entries"),
    #
    # path('medicine_list/', views.medicine_list, name="medicine_list"),
    # path('delete_medicine/', views.delete_medicine, name="delete_medicine"),
    # path('medicine_list/add_medicine/', views.add_medicine, name="add_medicine"),

]
