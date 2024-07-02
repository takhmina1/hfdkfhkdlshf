from django.contrib import admin
from .models import FAQ, ExchangeRule, KYCAMLCheck, CurrencyNews, OneMoment, Contact, Contest,Footer, Review
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    search_fields = ('title', 'text')
    list_filter = ('language',)
@admin.register(ExchangeRule)
class ExchangeRuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    search_fields = ('title', 'text')
    list_filter = ('language',)
@admin.register(KYCAMLCheck)
class KYCAMLCheckAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    search_fields = ('title', 'text')
    list_filter = ('language',)
@admin.register(CurrencyNews)
class CurrencyNewsAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'date')
    search_fields = ('language', 'title', 'content')
@admin.register(OneMoment)
class OneMomentAdmin(admin.ModelAdmin):
    list_display = ('language', 'name', 'text')
    search_fields = ('language', 'name', 'text')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'sender', 'timestamp')
    search_fields = ('email', 'sender', 'message')
    list_filter = ('timestamp',)
@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('end_time', 'participants', 'prize_amount', 'language')
    search_fields = ('participation_instructions', 'url')
    list_filter = ('language', 'end_time', 'deadline')
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('urls','image')
    search_fields = ('urls','image',)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_posted')  # Customize what fields to display in the admin list view
    search_fields = ('author', 'content')  # Add fields for searching
    list_filter = ('date_posted',)  # Add filters for date_posted
admin.site.register(Review, ReviewAdmin)
