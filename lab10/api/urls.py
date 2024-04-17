from django.urls import path
from .views import CompanyList, CompanyDetail, CompanyVacancyList, VacancyList, VacancyDetail, TopTenVacancies, CompanyCreate, VacancyCreate, CompanyUpdate, VacancyUpdate, CompanyDelete, VacancyDelete

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/create/', CompanyCreate.as_view(), name='company-create'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:pk>/update/', CompanyUpdate.as_view(), name='company-update'),
    path('companies/<int:pk>/delete/', CompanyDelete.as_view(), name='company-delete'),
    path('companies/<int:id>/vacancies/', CompanyVacancyList.as_view(), name='company-vacancy-list'),
    path('vacancies/', VacancyList.as_view(), name='vacancy-list'),
    path('vacancies/create/', VacancyCreate.as_view(), name='vacancy-create'),
    path('vacancies/<int:pk>/', VacancyDetail.as_view(), name='vacancy-detail'),
    path('vacancies/<int:pk>/update/', VacancyUpdate.as_view(), name='vacancy-update'),
    path('vacancies/<int:pk>/delete/', VacancyDelete.as_view(), name='vacancy-delete'),
    path('vacancies/top_ten/', TopTenVacancies.as_view(), name='top-ten-vacancies'),
]
