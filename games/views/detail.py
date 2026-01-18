from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from ..models import Game


@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    # 게임 참가자만 접근 가능
    if request.user not in (game.attacker, game.defender) and not request.user.is_superuser:
        raise Http404()

    can_counter = (
        request.user == game.defender
        and game.status == Game.Status.PENDING
    )

    context = {
        "game": game,
        "can_counter": can_counter,
    }
    return render(request, "games/detail.html", context)
