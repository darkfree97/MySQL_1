from django.shortcuts import render, render_to_response, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import DepartmentSerializer


def company_information(request):
    return render(request, "Strahova/company_information.html", {'title': 'Про нас', "info": CompanyInformation.objects.all()})


def news(request):
    return render(request, 'Strahova/news.html', {'title': 'Новини', 'news': News.objects.all()})


def services(request):
    return render(request, 'Strahova/services.html', {'title': 'Послуги', 'services': Services.objects.all()})


def departments(request):
    return render(request, 'Strahova/departments.html', {'title': 'Представництва', 'departments': DepartmentsMap.objects.all()})


def search_dep(request):
    if request.method == 'POST':
        region = request.POST['region']
        try:
            mydict = dict(DepartmentsMap.REGION_TYPE_CHOICES)
            region = list(mydict.keys())[list(mydict.values()).index(region)]
        except ValueError:
            region = request.POST['region']
        district = request.POST['district']
        city = request.POST['city']
    else:
        region = ''
        district = ''
        city = ''
    _departments = DepartmentsMap.objects.filter(
        region__contains=region,
        district__contains=district,
        city__contains=city
    )
    return render_to_response('Strahova/search_dep.html', {'departments': _departments})


def search_service(request):
    if request.method == 'POST':
        service_id = request.POST['service_id']
    else:
        service_id = -1
    service = get_object_or_404(Services, pk=service_id)
    return render_to_response('Strahova/service_descript.html', {'service': service})


class DepartmentList(APIView):
    def get(self, request):
        departments_v = DepartmentsMap.objects.all()
        serializer = DepartmentSerializer(departments_v, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(DepartmentsMap.objects.all(), many=True)
        return Response(serializer.data)
