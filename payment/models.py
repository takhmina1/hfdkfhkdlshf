from django.db import models

# Create your models here.
from django.db import models

class Payment(models.Model):
    """
    Модель для хранения информации о платеже.
    """
    email = models.EmailField(max_length=255, verbose_name='Email')
    fio_sender = models.CharField(max_length=100, verbose_name='ФИО отправителя')
    sberbank_card = models.CharField(max_length=18, verbose_name='Карта Сбербанка')
    tether_wallet = models.CharField(max_length=100, verbose_name='Кошелек Tether (TRC20)')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа')
    currency = models.CharField(max_length=3, verbose_name='Валюта платежа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=20, choices=[
        ('created', 'Создан'),
        ('approved', 'Одобрен'),
        ('failed', 'Неуспешный'),
        ('completed', 'Завершен'),
    ], default='created', verbose_name='Статус платежа')

    def __str__(self):
        return f'Payment {self.id} - {self.email} - {self.amount} {self.currency}'

class PaymentTransaction(models.Model):
    """
    Модель для хранения информации о транзакции платежа.
    """
    payment = models.ForeignKey(Payment, related_name='transactions', on_delete=models.CASCADE, verbose_name='Платеж')
    transaction_id = models.CharField(max_length=255, verbose_name='ID транзакции')
    status = models.CharField(max_length=20, choices=[
        ('created', 'Создан'),
        ('approved', 'Одобрен'),
        ('failed', 'Неуспешный'),
        ('completed', 'Завершен'),
    ], default='created', verbose_name='Статус транзакции')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'Transaction {self.transaction_id} - {self.status}'
