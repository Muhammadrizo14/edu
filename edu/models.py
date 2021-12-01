from django.db import models
from django.urls import reverse


class Edu(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя ученика')
    lastname = models.CharField(max_length=150, verbose_name='Фамилия ученика')
    age = models.IntegerField(default=0, verbose_name='Лет ученика')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Кружок')
    days = models.ForeignKey('Days', on_delete=models.PROTECT, null=True, verbose_name='Дни кружок')
    money = models.ForeignKey('Money', on_delete=models.PROTECT, null=True, verbose_name='Ежемесячный платеж')
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, null=True, verbose_name='Учители')
    phone = models.CharField(max_length=150, default=0, verbose_name='Телефон номер ученика')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"edu_id": self.pk})

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование кружка')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружоки'

class Days(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Дни кружка')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

class Money(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Платеж за месяц')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

class Teacher(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Учители')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учители'

