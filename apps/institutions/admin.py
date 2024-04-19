from django.contrib import admin
from apps.institutions.models import Institution,InstitutionService,TypeService,TypeInstitution
# Register your models here.

admin.site.register(Institution)
admin.site.register(InstitutionService)
admin.site.register(TypeService)
admin.site.register(TypeInstitution)
