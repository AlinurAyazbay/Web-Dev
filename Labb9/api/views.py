from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company, Vacancy, List
from .serializers import CompanySerializer, ListSerializer, VacancySerializer


@api_view(['GET'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def company_detail(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

@api_view(['GET'])
def company_vacancies(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(pk=id)
    except Vacancy.DoesNotExist:
        return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

@api_view(['GET'])
def vacancy_top_ten(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def vacancy_name(request):
    if request.method == 'GET':
        List_of_jobs = List.objects.all()
        serializer = ListSerializer(List_of_jobs, many = True)
        return Response(serializer.data)
        
        