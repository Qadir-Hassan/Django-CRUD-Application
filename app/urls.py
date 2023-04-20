from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.insert_page_view,name="insert-page-view"),
   path("insert/",views.insert_data,name="insert"),
   path("show/",views.show_data,name="show"),
   path("edit/<int:pk>",views.edit_data,name="edit"),
   path("update/<int:pk>",views.update_data,name="update"),

   path("delete/<int:pk>",views.delete_data,name="delete"),

   #dummy
   path("insert2/",views.insert2,name="insert2"),
   
]
