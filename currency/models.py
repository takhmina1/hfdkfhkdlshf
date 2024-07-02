from django.db import models

class FiatCurrency(models.Model):
    assetCode = models.CharField(max_length=10)  # Код валюты (например, USD)
    assetName = models.CharField(max_length=255)  # Название валюты
    assetLogo = models.URLField()  # URL-адрес логотипа валюты
    size = models.IntegerField()  # Размер валюты (например, 2 для копеек, 100 для центов)
    fiatMinLimit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Минимальный лимит для фиатных операций
    fiatMaxLimit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
 # Максимальный лимит для фиатных операций
    cryptoMinLimit = models.DecimalField(max_digits=15, decimal_places=8, null=True, blank=True)  # Минимальный лимит для криптовалютных операций
    cryptoMaxLimit = models.DecimalField(max_digits=15, decimal_places=8, null=True, blank=True)  # Максимальный лимит для криптовалютных операций
    quotation = models.CharField(max_length=255, null=True, blank=True)  # Котировка валюты
    suggestAmounts = models.JSONField(null=True, blank=True)  # Рекомендованные суммы для операций

    def __str__(self):
        return f"{self.assetName} ({self.assetCode})"  # Возвращает строковое представление объекта

    class Meta:
        verbose_name = "Фиатная валюта"  # Название модели в единственном числе
        verbose_name_plural = "Фиатные валюты"  # Название модели во множественном числе


class Coin(models.Model):
    coin = models.CharField(max_length=50)  # Код криптовалюты
    name = models.CharField(max_length=100)  # Название криптовалюты
    deposit_status_all = models.BooleanField()  # Статус возможности депозита для всех сетей
    receive_status_all = models.BooleanField()  # Статус возможности получения для всех сетей
    default_form_value = models.CharField(max_length=50)  # Значение по умолчанию для формы

    def __str__(self):
        return self.name  # Возвращает название криптовалюты при обращении к объекту

    class Meta:
        verbose_name = "Криптовалюта"  # Название модели в единственном числе
        verbose_name_plural = "Криптовалюты"  # Название модели во множественном числе


class Network(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='networks')  # Ссылка на криптовалюту
    name = models.CharField(max_length=100)  # Название сети
    deposit = models.BooleanField()  # Статус возможности депозита
    receive = models.BooleanField()  # Статус возможности получения
    is_default = models.BooleanField()  # Является ли сеть сетью по умолчанию
    confirmations_minimum = models.IntegerField()  # Минимальное количество подтверждений
    confirmations_maximum = models.IntegerField()  # Максимальное количество подтверждений
    withdraw_decimals_minimum = models.IntegerField()  # Минимальное количество десятичных разрядов при выводе
    regex_address = models.CharField(max_length=255)  # Регулярное выражение для проверки адреса
    regex_tag = models.CharField(max_length=255, blank=True, null=True)  # Регулярное выражение для проверки тега (если есть)
    has_tag = models.BooleanField()  # Наличие тега у сети
    tag_name = models.CharField(max_length=50, blank=True, null=True)  # Название тега (если есть)
    explorer = models.URLField(max_length=200)  # Ссылка на исследователь блоков
    explorer_hash = models.URLField(max_length=200)  # Ссылка на транзакцию в исследователе блоков
    explorer_address = models.URLField(max_length=200)  # Ссылка на адрес в исследователе блоков
    confirmation_minutes_range = models.CharField(max_length=20)  # Диапазон времени подтверждения

    def __str__(self):
        return f"{self.coin.name} - {self.name}"  # Возвращает строковое представление сети


class Transaction(models.Model):
    wallet = models.CharField(max_length=255, help_text="Кошелёк, например, 'кошелёк мбанк мобильный кошелёк'")  # Кошелёк отправителя
    send_currency = models.CharField(max_length=50, choices=[
        ('fiat', 'Фиатная валюта'), 
        ('crypto', 'Криптовалюта')
    ], help_text="Тип отправляемой валюты")  # Тип отправляемой валюты
    send_amount = models.DecimalField(max_digits=20, decimal_places=8, help_text="Отправляемая сумма")  # Отправляемая сумма
    receive_currency = models.CharField(max_length=50, choices=[
        ('fiat', 'Фиатная валюта'), 
        ('crypto', 'Криптовалюта')
    ], help_text="Тип получаемой валюты")  # Тип получаемой валюты
    receive_amount = models.DecimalField(max_digits=20, decimal_places=8, help_text="Получаемая сумма")  # Получаемая сумма
    fee = models.DecimalField(max_digits=10, decimal_places=2, help_text="Комиссия за транзакцию")  # Комиссия за транзакцию
    send_method = models.CharField(max_length=255, help_text="Способ отправки, например, 'банки, есть там сбербанка или киви'")  # Способ отправки
    receive_method = models.CharField(max_length=255, help_text="Способ получения, например, 'денег, криптовалюта'")  # Способ получения
    transaction_date = models.DateTimeField(auto_now_add=True)  # Дата и время транзакции

    def __str__(self):
        return f"Transaction from {self.send_currency} to {self.receive_currency} on {self.transaction_date}"  # Возвращает строковое представление транзакции

    class Meta:
        verbose_name = "Транзакция"  # Название модели в единственном числе
        verbose_name_plural = "Транзакции"  # Название модели во множественном числе


# """ конвертировать """







