"berries api urls module"
from berries.api import views
from django.urls import path, include
from pokeberries.api.routers import PokeberriesRouter

router = PokeberriesRouter()
router.APIRootView = views.BerriesRootView


app_name = "berries-api"

urlpatterns = [
    path("allBerryStats", views.BerryStatsView.as_view(), name="stats"),
    path("", include(router.urls)),
]