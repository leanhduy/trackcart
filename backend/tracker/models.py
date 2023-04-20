from django.db import models
from account.models import Profile

# Create your models here.


class Category(models.Model):
    TYPE_CHOICES = (("income", "Income"), ("expense", "Expenses"))
    SUB_CATEGORIES = (
        ("required", "Required Expenses"),
        ("comingup", "Up & Comers"),
        ("entertainment", "Fun & Relax"),
        ("investing", "Investing & Debt Payments"),
        ("income", "Income"),
        ("other", "Other"),
    )
    name = models.CharField(max_length=255)
    featured_icon = models.FileField(null=True, blank=True)
    cate_type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    sub_category = models.CharField(
        max_length=50, choices=SUB_CATEGORIES, null=False, blank=False
    )

    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self) -> str:
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=255)
    iso = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Currencies"
    
    def __str__(self) -> str:
        return self.name


class Wallet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Wallets"
        
    def __str__(self) -> str:
        return self.name


class Transaction(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField()

    class Meta:
        verbose_name_plural = "Transactions"
        
    def __str__(self) -> str:
        return self.name
