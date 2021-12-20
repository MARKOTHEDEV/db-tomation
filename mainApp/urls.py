from django.urls import path

from . import views

urlpatterns = [
       path('',views.index,name='homePage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('solution/<int:pk>/',views.solutionDetail,name='solutionDetail'),
    path('join-pather-ship-network/',views.joinPatherShipNetwork,name='joinPatherShipNetwork'),
    path('work-with-emetrics/',views.workWithEmetrics,name='work-with-emetric'),
    path('insight/',views.all_insightPage,name='list-of-insight'),
    path('our-team/',views.our_team,name='our_team'),
    path("locations/",views.locations,name='locations')
]