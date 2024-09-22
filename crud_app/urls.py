from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('view/',views.view,name='view'),
    path('addrecord/',views.addrecord,name='addrecord'),
    path('view/delete/<int:id>/',views.delete_item,name='delete'),
    path('view/update/<int:id>/',views.update,name='update'),
    path('view/update/update_record/<int:id>/',views.update_record,name='update_record'),
]