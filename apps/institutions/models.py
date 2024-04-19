from django.db import models
from utils.validates.validates import validate_address, validate_letters_numbers_and_spaces
from django.core.validators import MinLengthValidator
from apps.abstract.models import Base, ServiceWeekBase, WeekBase



class TypeInstitution(models.Model):
    """docstring for TypeInstitution."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    
 
    class Meta:
        verbose_name= 'Tipo de institución'
        verbose_name_plural= 'Tipos de instituciones'
        
    def __str__(self) -> str:
        return self.name
    
# Institution model
class Institution(Base,WeekBase):
    """docstring for Institution."""
    image = models.ImageField('Imagen',upload_to='institucion/',null=False,blank=False)
    type_institution = models.ForeignKey(TypeInstitution, on_delete = models.CASCADE , verbose_name='Tipo de institución')
    
    
    class Meta:
        verbose_name= 'Institución'
        verbose_name_plural= 'Instituciones'
        
    def __str__(self) -> str:
        return f'{self.name}'


class InstitutionService(ServiceWeekBase):
    """docstring for InstitutionService."""
    type_service = models.ForeignKey('TypeService', on_delete = models.CASCADE , verbose_name='Tipo de servicio')
    institution = models.ForeignKey(Institution, on_delete = models.CASCADE , verbose_name='Institución')
    
    
    class Meta:
        verbose_name= 'Servicio de institución'
        verbose_name_plural= 'Servicios de instituciones'
        
    def __str__(self) -> str:
        return f'{self.name}'
    

class TypeService(models.Model):
    """docstring for TypeService."""
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    
 
    class Meta:
        verbose_name= 'Tipo de servicios'
        verbose_name_plural= 'Tipos de servicios'
        
    def __str__(self) -> str:
        return self.name
    

    
    

    

