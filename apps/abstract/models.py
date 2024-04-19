from django.db import models
from utils.validates.validates import validate_digits,validate_letters_numbers_and_spaces,validate_address,validate_text
from django.core.validators import MinLengthValidator


class Base(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    """docstring for Base."""
    class Meta:
        abstract = True


class WeekBase(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Domingo'),
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
    )
    in_time = models.TimeField('Hora inicial',null= False, blank=False)
    out_time = models.TimeField('Hora final',null= False, blank=False)
    init_day_of_week = models.IntegerField(
        'Dia inicial del servicio',
        default=0,
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    end_day_of_week = models.IntegerField(
        'Dia final del servicio',
        default=6,
        choices=DAYS_OF_WEEK,
        help_text="Selecciona el dia de la semana."
    )
    
    """docstring for WeekBase."""
    class Meta:
        abstract = True



class ServiceWeekBase(models.Model):
    DAYS_OF_WEEK = (
        ('Domingo', 'Domingo'),
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
    )
    
    name = models.CharField('Nombre',validators=[MinLengthValidator(3),validate_letters_numbers_and_spaces], max_length=255, blank=False , null=False, unique=True)
    description = models.TextField('Descripción',validators=[MinLengthValidator(3),validate_text],max_length=255, blank=False , null=False)
    in_time = models.TimeField('Hora inicial',null= False, blank=False)
    out_time = models.TimeField('Hora final',null= False, blank=False)
    active = models.BooleanField('Activo', default=True)
    init_day_of_week = models.CharField(
        'Dia inicial del servicio',
        default='Domingo',
        choices=DAYS_OF_WEEK,
        max_length=9,
        help_text="Selecciona el dia de la semana."
    )
    end_day_of_week = models.CharField(
        'Dia final del servicio',
        default='Domingo',
        choices=DAYS_OF_WEEK,
        max_length=9,
        help_text="Selecciona el dia de la semana."
    )
    
    """docstring for ServiceWeekBase."""
    class Meta:
        abstract = True
