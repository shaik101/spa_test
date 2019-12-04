from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('addcity/',views.addcity,name='addcity'),
    path('guest/',views.guest,name='guest'),
    path('guest_list/',views.guest_list,name='guest_list'),
    path('gift/',views.gifts,name='gifts'),
    path('addstaff/',views.addstaff,name='addstaff'),
    path('addstaff/updates/<int:id>',views.updates,name='updates'),


    path('carriers/',views.carriers,name='carriers'),
    path('addcity/update/<int:id>',views.update,name='update'),
    path('appointment',views.appointment,name='adminappointment'),
    path('addcity/delete/<int:id>',views.delete,name='delete'),
    path('appointment/deleted/<int:id>',views.deleted,name='deleted'),
    path('addservice/',views.addservice,name='addservice'),
    path('addservice/modify/<int:id>',views.modify,name='modify'),
    path('addservice/deletes/<int:id>',views.deletes,name='deletes'),
    path('admin_login/',views.admin_login,name='admin_login'),







    # path('edit/<int:city_id>',views.edit,name='edit')

]
