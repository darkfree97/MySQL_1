from django.conf.urls import url

from . import views

app_name = "Strahova"

urlpatterns = [
    url(r'^$', views.company_information, name="info"),
    url(r'^departments/$', views.departments, name="departments"),
    url(r'^services/$', views.services, name="services"),
    url(r'^news/$', views.news, name="news"),
    url(r'^search_dep/$', views.search_dep, name="search_dep"),
    url(r'^service_description/$', views.search_service, name="service_description"),
    url(r'^depapi/', views.DepartmentList.as_view()),
]
