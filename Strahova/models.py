from django.db import models
from django.core.urlresolvers import reverse


class CompanyInformation(models.Model):
    information = models.TextField(verbose_name="Інформація")
    image = models.ImageField(upload_to='images', default=None, null=True, blank=True, verbose_name="Картинка")

    class Meta:
        verbose_name_plural = "Інформація про компанію"

    def get_absolute_url(self):
        return reverse('Strahova:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.information


class News(models.Model):
    description = models.TextField(verbose_name="Опис новини")
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name_plural = "Новини"

    def get_absolute_url(self):
        return reverse('Strahova:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.description


class Services(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва послуги")
    description = models.TextField(verbose_name="Опис послуги")
    image = models.ImageField(upload_to='images', default=None, verbose_name="Картинка")

    class Meta:
        verbose_name_plural = "Послуги"

    def get_absolute_url(self):
        return reverse('Strahova:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.description


class DepartmentsMap(models.Model):
    REGION_TYPE_CHOICES = (
        ('0', 'Київська'),
        ('1', 'АР Крим'),
        ('2', 'Вінницька'),
        ('3', 'Волинська'),
        ('4', 'Дніпровська'),
        ('5', 'Донецька'),
        ('6', 'Житомирська'),
        ('7', 'Закарпатська'),
        ('8', 'Запорізька'),
        ('9', 'Івано-Франківська'),
        ('10', 'Кіровоградська'),
        ('11', 'Луганська'),
        ('12', 'Львівська'),
        ('13', 'Миколаївська'),
        ('14', 'Одеська'),
        ('15', 'Полтавська'),
        ('16', 'Рівненська'),
        ('17', 'Сумська'),
        ('18', 'Тернопільська'),
        ('19', 'Харківська'),
        ('20', 'Херсонська'),
        ('21', 'Хмельницька'),
        ('22', 'Черкаська'),
        ('23', 'Чернівецька'),
        ('24', 'Чернігівська')
    )
    region = models.CharField(max_length=2, choices=REGION_TYPE_CHOICES, verbose_name="Область")
    district = models.CharField(max_length=100, verbose_name="Район")
    city = models.CharField(max_length=100, verbose_name="Місто")
    address = models.CharField(max_length=255, verbose_name="Вулиця, будинок")
    photo = models.ImageField(upload_to='images', default=None, verbose_name="Зображення відділення")

    class Meta:
        verbose_name_plural = "Філіали"

    def get_absolute_url(self):
        return reverse('Strahova:detail', kwargs={'pk': self.pk})

    def get_region(self):
        return self.REGION_TYPE_CHOICES[int(self.region)][1]

    def __str__(self):
        return self.get_region()+" обл. "+self.district+" р-н.  м."+self.city+" "+self.address
