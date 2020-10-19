from django.urls import path
from .views import t_company, home

urlpatterns = [
    path('', home.home, name='home'),
    # path('', t_company.company_list, name='company')
]
