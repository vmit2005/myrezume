from django.db import models

class Rezume(models.Model):
    title = models.CharField(max_length=100, verbose_name='Место работы')
    date1 = models.CharField(max_length=20, verbose_name='Дата1')
    date2 = models.CharField(max_length=20,blank=True, verbose_name='Дата2')
    description = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.title


class Acad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='rezume/media/')
    url= models.URLField(blank=True)

    def __str__(self):
        return self.title

class Arbeit(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=500,verbose_name='Описание')
    drawing = models.FileField(upload_to='arbeit/media/',blank=True, verbose_name='Чертеж')
    dr_spec = models.FileField(upload_to='arbeit/media/', blank=True, verbose_name='Спецификация')
    dr_model = models.FileField(upload_to='arbeit/media/', blank=True, verbose_name='Модель')

    def __str__(self):
        return self.title


class Proggg(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание программы' )
    url = models.URLField(blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title


