from django.urls import path
from . import views


urlpatterns = [

    path('',views.login_user,name='login_user'),
    path('register/',views.register_page,name='register_page'),
    path('save_details/',views.save_details,name='save_details'),
    path('login_sucess_or_not/',views.login_sucess_or_not,name='login_sucess_or_not'),
    path('items/',views.items,name='items'),
    path('<int:receipe_id>/details/',views.details,name='details'),
    path('create_page/',views.create_page,name='create_page'),
    path('save_receipe/',views.save_receipe,name='save_receipe'),
    path('<int:receipe_id>/delete_receipe/',views.delete_receipe,name='delete_receipe'),
    path('logout_page/',views.logout_page,name='logout_page'),

]