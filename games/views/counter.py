import random
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

from ..models import Game
from ..services import resolve_game

@login_required
def counterattack(request, pk):
    game = get_object_or_404(Game, pk=pk)

    # 수비자만 가능
    if request.user != game.defender and not request.user.is_superuser:
        raise Http404()

    # 이미 끝난 게임이면 상세로
    if game.status != Game.Status.PENDING:
        return redirect("games:detail", pk=pk)

    session_key = f"counter_cards_{pk}"

    # GET: 카드 5장 제공
    if request.method == "GET":
        cards = random.sample(range(1, 11), 5)
        request.session[session_key] = cards
        return render(request, "games/counter.html", {
            "game": game,
            "cards": cards,
        })

    # POST: 결과 계산
    cards = request.session.get(session_key, [])
    selected = int(request.POST.get("card"))

    if selected not in cards:
        raise Http404()

    resolve_game(
        game_id=pk,
        defender_user=request.user,
        defender_card=selected,
    )

    request.session.pop(session_key, None)
    return redirect("games:detail", pk=pk)
