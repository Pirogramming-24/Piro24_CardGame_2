from django.urls import path

from .views.detail import game_detail
from .views.counter import counterattack
from .views.ranking import ranking

app_name = "games"

urlpatterns = [
    path("detail/<int:pk>/", game_detail, name="detail"),
    path("counter/<int:pk>/", counterattack, name="counter"),
    path("ranking/", ranking, name="ranking"),
]
