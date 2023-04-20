from rest_framework.response import Response
from rest_framework.decorators import api_view
from tracker.serializers import CurrencySerializer
from tracker.models import Currency

# Create your views here.
@api_view(['GET'])
def get_all_currencies(request):
    currencies = Currency.objects.all()
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_single_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    serializer = CurrencySerializer(currency, many=False)
    return Response(serializer.data)