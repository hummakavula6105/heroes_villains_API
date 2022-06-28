from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SupersSerializer
from .models import Super

@api_view(['GET'])
def supers_list(request):
    supers = Super.objects.all()

    serializer = SupersSerializer(supers, many=True)



    return Response (serializer.data)