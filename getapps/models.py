from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from transliterate import translit

LANG_CHOICES = (
    ("en", "English"),
    ("ru", "Русский язык")
)
class FAQ(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    def str(self):
        return self.title
    def save(self, *args, **kwargs):
        target_language = kwargs.pop('target_language', None)
        if target_language:
            if self.language == 'en' and target_language == 'ru':
                self.title = translit(self.title, 'ru', reversed=True)
                self.text = translit(self.text, 'ru', reversed=True)
            elif self.language == 'ru' and target_language == 'en':
                self.title = translit(self.title, 'ru', reversed=False)
                self.text = translit(self.text, 'ru', reversed=False)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
class ExchangeRule(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    def str(self):
        return self.title
    def save(self, *args, **kwargs):
        target_language = kwargs.pop('target_language', None)
        if target_language:
            if self.language == 'en' and target_language == 'ru':
                self.title = translit(self.title, 'ru', reversed=True)
                self.text = translit(self.text, 'ru', reversed=True)
            elif self.language == 'ru' and target_language == 'en':
                self.title = translit(self.title, 'ru', reversed=False)
                self.text = translit(self.text, 'ru', reversed=False)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Правило обмена"
        verbose_name_plural = "Правила обмена"
class KYCAMLCheck(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    text = models.TextField(verbose_name=_('Текст'))
    def save(self, *args, **kwargs):
        target_language = kwargs.pop('target_language', None)
        if target_language:
            if self.language == 'en' and target_language == 'ru':
                self.title = translit(self.title, 'ru', reversed=True)
                self.text = translit(self.text, 'ru', reversed=True)
            elif self.language == 'ru' and target_language == 'en':
                self.title = translit(self.title, 'ru', reversed=False)
                self.text = translit(self.text, 'ru', reversed=False)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = _('KYC/AML Запись')
        verbose_name_plural = _('KYC/AML Записи')
class CurrencyNews(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        target_language = kwargs.pop('target_language', None)
        if target_language:
            if self.language == 'en' and target_language == 'ru':
                self.title = translit(self.title, 'ru', reversed=True)
                self.content = translit(self.content, 'ru', reversed=True)
            elif self.language == 'ru' and target_language == 'en':
                self.title = translit(self.title, 'ru', reversed=False)
                self.content = translit(self.content, 'ru', reversed=False)
        super(CurrencyNews, self).save(*args, **kwargs)

class OneMoment(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="имя")
    text = models.CharField(max_length=100, verbose_name="Текст")

    class Meta:
        verbose_name = "Один момент"
        verbose_name_plural = "Одни моменты"

    def save(self, *args, **kwargs):
        target_language = kwargs.pop('target_language', None)
        if target_language:
            if self.language == 'en' and target_language == 'ru':
                self.name = translit(self.name, 'ru', reversed=True)
                self.text = translit(self.text, 'ru', reversed=True)
            elif self.language == 'ru' and target_language == 'en':
                self.name = translit(self.name, 'ru', reversed=False)
                self.text = translit(self.text, 'ru', reversed=False)
        super(OneMoment, self).save(*args, **kwargs)

class Contact(models.Model):
    email = models.EmailField(verbose_name='Адрес электронной почты')
    website = models.URLField(verbose_name='Веб-сайт', blank=True, null=True)
    sender = models.EmailField(verbose_name='Отправитель')
    message = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='Временная метка')
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Contest(models.Model):
    language = models.CharField('Язык', choices=LANG_CHOICES, default='en', max_length=255, null=True, blank=True)
    participants = models.IntegerField(default=15, verbose_name="Количество участников")
    prize_amount = models.DecimalField(max_digits=10, decimal_places=2, default=1300, verbose_name="Банк конкурса")
    end_time = models.DateTimeField(verbose_name="Время окончания")
    deadline = models.DateTimeField(verbose_name="Срок завершения", null=True, blank=True)
    participation_instructions = models.TextField(
        default="\n1. Совершить обмен на нашем сервисе onemoment.cc\n2. Подписаться на телеграмм канал @onemomentinfo\n3. Написать отзыв на bestchange.ru в день совершения обмена\n4. Убедиться в том, что номер обмена и email в отзыве совпадают с email, который указывался в заявке на обмен\n5. Проверить результаты розыгрыша в пятницу 18:00 в нашем телеграм канале @onemomentinfo",
        verbose_name="Инструкции по участию"
    )
    url = models.URLField(verbose_name="URL", null=True, blank=True)

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"

    def save(self, *args, **kwargs):
        self.participants += 1
        self.prize_amount = self.participants * 100
        if not self.deadline:
            self.deadline = self.end_time
        super(Contest, self).save(*args, **kwargs)

        target_language = kwargs.pop('target_language', None)
        if target_language:
            if self.language == 'en' and target_language == 'ru':
                self.title = translit(self.title, 'ru', reversed=True)
                self.participation_instructions = translit(self.participation_instructions, 'ru', reversed=True)
            elif self.language == 'ru' and target_language == 'en':
                self.title = translit(self.title, 'ru', reversed=False)
                self.participation_instructions = translit(self.participation_instructions, 'ru', reversed=False)
            super(Contest, self).save(*args, **kwargs)
class Footer(models.Model):
    urls = models.URLField(verbose_name="URL", null=True, blank=True)
    image = models.ImageField(upload_to='footer_images/', verbose_name="Image", null=True, blank=True)

    class Meta:
        verbose_name = "Веб-сайт"
        verbose_name_plural = "Веб-сайт"

class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор отзыва')
    content = models.TextField(verbose_name='Текст отзыва')
    date_posted = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
