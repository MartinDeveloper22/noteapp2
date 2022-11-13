from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.note_form,name='insert'),
   path('search/',views.note_search,name='searchbyid'),
   path('delete/<int:id>',views.note_del,name='del'),
    path('list/',views.note_list,name='list'),#localhost:Port/note/list
]
