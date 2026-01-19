from django.urls import path
from .views.main import main
from .views.attack import attack
from .views.list import game_list
from .views.detail import game_detail
from .views.counter import counterattack
from .views.delete import delete_game
from .views.ranking import ranking

app_name = "games"

urlpatterns = [
    path("", main, name="main"),
    path("attack/", attack, name="attack"),
    path("list/", game_list, name="list"),
    path("detail/<int:pk>/", game_detail, name="detail"),
    path("counter/<int:pk>/", counterattack, name="counter"),
    path("delete/<int:pk>/", delete_game, name="delete"),
    path("ranking/", ranking, name="ranking"),
]
