"Main Pokeberries api views module"
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):
    def get_view_name(self):
        return "API Root"

    def get(self, request, format=None):
        return Response({
            # register all api urls
            "berries": reverse("berries-api:api-root", request=request, format=format),
        })
