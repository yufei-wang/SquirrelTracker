from django.urls import path

from . import views

urlpatterns = [
        path('',views.home),
        path('map/',views.map),
        path('sightings/', views.sightings,name='sightings'),
        path('<str:unique_squirrel_id>',views.squirrel_id,name='squirrel_id'),
        path('add/', views.add, name='add'),
        path('stats/', views.stats,name='stats'),        
        ]
