from django.shortcuts import render
from apps.institutions.models import Institution,InstitutionService
# Create your views here.

def institution_list(request):
    institution = Institution.objects.filter(active = True)

    context = {
        'institution' : institution,
    }

    return render(request,'institution_list_view.html',context)

def institution_detail(request,pk):
    institution = Institution.objects.filter(
        pk = pk,
        active = True).first()
    services = InstitutionService.objects.filter(
        institution = institution,
        active = True
    )
    context = {
        'institution':institution,
        'services':services,
    }

    return render(request,'institution_detail_view.html',context)


