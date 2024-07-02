from django.db import models
from django.utils.translation import gettext_lazy as _
from transliterate import translit

LANG_CHOICES = (
    ("en", "English"),
    ("ru", "Русский язык")
)
class Application(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True,blank=True)
    number = models.CharField(max_length=100, verbose_name="Номер")
    date = models.DateField(verbose_name="Дата")
    direction = models.CharField(max_length=100, verbose_name="Направление")
    direct = models.CharField(max_length=100, verbose_name="Направление")
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

class Discount(models.Model):
    start_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="От")
    end_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="До")
    percentage = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Процент")

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        if self.end_amount:
            return f"{self.start_amount}$ - {self.end_amount}$: {self.percentage}%"
        else:
            return f"Больше {self.start_amount}$: {self.percentage}%"

# Добавляем данные таблицы скидок
Discount.objects.bulk_create([
    Discount(start_amount=0, end_amount=500, percentage=0.08),
    Discount(start_amount=500, end_amount=1000, percentage=0.10),
    Discount(start_amount=1000, end_amount=2000, percentage=0.12),
    Discount(start_amount=2000, end_amount=4000, percentage=0.14),
    Discount(start_amount=4000, end_amount=6000, percentage=0.16),
    Discount(start_amount=6000, end_amount=10000, percentage=0.18),
    Discount(start_amount=10000, percentage=0.20),
])

class Program(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="имя")
    text = models.CharField(max_length=100, verbose_name="Текст")
    participation_instructions = models.TextField(verbose_name="Инструкции по участию")
    url = models.URLField(verbose_name="URL", null=True, blank=True)
    class Meta:
        verbose_name = "Реферальная программа"
        verbose_name_plural = "Реферальная программа"