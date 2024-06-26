from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from skus.models import Sku
from skus.serializers import SkuSerializer

@csrf_exempt
def sku_list(request):
    """
    List all code skus, or create a new sku.
    """
    if request.method == 'GET':
        skus = Sku.objects.all()
        serializer = SkuSerializer(skus, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SkuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def sku_detail(request, pk):
    """
    Retrieve, update or delete a code sku.
    """
    try:
        sku = Sku.objects.get(pk=pk)
    except Sku.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkuSerializer(sku)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkuSerializer(sku, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sku.delete()
        return HttpResponse(status=204)