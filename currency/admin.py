from django.contrib import admin
from .models import FiatCurrency, Coin, Network

# Регистрация модели FiatCurrency
@admin.register(FiatCurrency)
class FiatCurrencyAdmin(admin.ModelAdmin):
    list_display = ('assetCode', 'assetName', 'assetLogo', 'size', 'fiatMinLimit', 'fiatMaxLimit', 'cryptoMinLimit', 'cryptoMaxLimit', 'quotation')
    search_fields = ('assetCode', 'assetName')
    list_filter = ('size', 'quotation')
    # Добавьте другие необходимые настройки административной панели

# Регистрация модели Coin
@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('coin', 'name', 'deposit_status_all', 'receive_status_all', 'default_form_value')
    search_fields = ('coin', 'name')
    list_filter = ('deposit_status_all', 'receive_status_all')
    # Добавьте другие необходимые настройки административной панели

# Регистрация модели Network
@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('coin', 'name', 'deposit', 'receive', 'is_default', 'confirmations_minimum', 'confirmations_maximum', 'withdraw_decimals_minimum', 'regex_address', 'has_tag', 'explorer', 'explorer_hash', 'explorer_address', 'confirmation_minutes_range')
    search_fields = ('coin__name', 'name')
    list_filter = ('deposit', 'receive', 'is_default')
    # Добавьте другие необходимые настройки административной панели
