from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET'])
def super_types_list(request):
    supers = SuperType.objects.all()

    serializer = SuperTypeSerializer(supers, many=True)



    return Response (serializer.data)