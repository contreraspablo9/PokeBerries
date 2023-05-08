"""Berries views module"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from rest_framework.reverse import reverse
from berries.api.berries_api import BerriesData


# web navigation views
class BerryStatsView(APIView):
    "Berry stats API root view"

    def get(self, request, format=None):
        "Return endpoint view"
        berries = BerriesData()
        data = {
            "berries_names":berries.names_list(),
            "min_growth_time":berries.min_growth_time(),
            "median_growth_time":berries.median_growth_time(),
            "max_growth_time":berries.max_growth_time(),
            "variance_growth_time":berries.variance_growth_time(),
            "mean_growth_time":berries.mean_growth_time(),
            "frequency_growth_times":berries.frequency_growth_time(),
        }
        return Response(data)

class BerriesRootView(APIRootView):
    """
    Berries API root view
    """
    def get_view_name(self):
        return "Berries"

    def get(self, request, format=None):
        return Response({
            # register all api urls
            "allBerryStats": reverse("berries-api:stats", request=request, format=format),
        })
