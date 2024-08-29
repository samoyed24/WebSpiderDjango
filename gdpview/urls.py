from django.urls import path

from gdpview import views

urlpatterns = [
    path('update/', views.update_data, name='update'),
    path('get-data/', views.get_gdp_data, name='get-data'),
    path('', views.index, name='index')
]
