from django.db import models

# Create your models here.
class Main(models.Model):
    site_name = models.CharField(verbose_name="Имя сайта", max_length=50)
    logo = models.ImageField(verbose_name="Логтоип Сайта", upload_to='logo/')

    def _str_(self):
        return self.site_name

    class Meta:
        verbose_name ='Настройка'
        verbose_name_plural = 'Настройки'

class AboutUs(models.Model):
    photo = models.ImageField(upload_to='about_photo/')
    description = models.TextField("Описание")
    year_in_business = models.IntegerField("Сколько лет мы в бизнесе")
    happy_people = models.IntegerField("Счастливые люди")
    sales = models.IntegerField("Продажи")
    award_winning = models.IntegerField("Награды")

    def _str_(self):
        return self.description

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Team(models.Model):
    photo = models.ImageField("Фотография", upload_to='team_photo/')
    name = models.CharField("Имя", max_length=50)
    job_title = models.CharField("Должность", max_length=100)
    instagram = models.URLField('Инстаграм')
    facebook = models.URLField("Фейсбук")

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Команда"


class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=300)
    photo = models.ImageField('Фото', upload_to='blog_photo/')
    description = models.TextField("Описание")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"



class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.subject

class CantactUs(models.Model):
    address = models.CharField('Адрес', max_length=100)
    phone_number1 = models.CharField('Номер телефона 1', max_length=100)
    phone_number2 = models.CharField('Номер телефона 2', max_length=100)
    email = models.EmailField('Почта')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'



