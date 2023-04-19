from django.contrib import admin
from tracker.models import Category, Currency, Wallet, Transaction


# Set up AdminModel classes for the models
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "featured_icon", "cate_type", "sub_category")


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "iso")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "amount", "wallet", "category", "date", "note")


class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "currency", "balance")


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Wallet, WalletAdmin)
