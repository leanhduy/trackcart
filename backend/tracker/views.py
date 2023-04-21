from rest_framework.response import Response
from rest_framework.decorators import api_view
from tracker.serializers import CurrencySerializer, CategorySerializer, WalletSerializer
from tracker.models import Currency, Category, Wallet


# Create your views here.
# * CURRENCY VIEWS
@api_view(["GET"])
def get_all_currencies(request):
    currencies = Currency.objects.all()
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    serializer = CurrencySerializer(currency, many=False)
    return Response(serializer.data)


# * CATEGORY VIEWS
@api_view(["GET"])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


# * WALLET VIEWS
@api_view(["GET"])
def get_all_wallets(request):
    wallets = Wallet.objects.all()
    serializer = WalletSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_wallet(request, pk):
    wallet = Wallet.objects.get(id=pk)
    serializer = WalletSerializer(wallet, many=False)
    return Response(serializer.data)
