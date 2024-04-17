from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy

def companies_list(request):
    companies = Company.objects.all()
    data = {"companies": list(companies.values())}
    return JsonResponse(data)

def company(request, id):
    company = get_object_or_404(Company, id=id)
    data = {
        "company": {
            "name": company.name,
            "description": company.description,
            "city": company.city,
            "address": company.address
        }
    }
    return JsonResponse(data)

def company_vacancies(request, id):
    company = get_object_or_404(Company, id=id)
    vacancies = company.vacancies.all()
    data = {
        "vacancies": list(vacancies.values())
    }
    return JsonResponse(data)

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    data = {
        "vacancies": list(vacancies.values())
    }
    return JsonResponse(data)

def vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    data = {
        "vacancy": {
            "name": vacancy.name,
            "description": vacancy.description,
            "salary": vacancy.salary,
            "company": vacancy.company.name
        }
    }
    return JsonResponse(data)
def top_ten_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {"vacancies": list(top_vacancies.values())}

    return JsonResponse(data)
