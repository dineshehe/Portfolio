from myport import views
from django.urls import path

urlpatterns = [
    path("", views.homepage, name = 'home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name="contact"),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name ='skills'),
    path('projects/', views.projects, name = 'projects'),

    #saving form

    path("saveData", views.savinginfo, name= 'saving'),
    path('records/', views.records, name = 'records'),

    #deleteing records

    path("deleteR/<int:x>", views.deleteR, name="deleteR"),

    #updating data

path('updating/<int:update_id>', views.updating, name='updating'),
path("updated/<int:update_id>", views.updated, name="updated")

]
