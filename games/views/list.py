from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

from ..models import Game

@login_required
def game_list(request):
    """
    게임 리스트 페이지 - 최신순 정렬
    내가 참여한 모든 게임을 최신순으로 표시
    """
    user = request.user
    
    # 내가 참여한 모든 게임 (공격자 또는 수비자)
    games = Game.objects.filter(
        Q(attacker=user) | Q(defender=user)
    ).select_related('attacker', 'defender').order_by('-created_at')
    
    return render(request, "games/list.html", {
        "games": games,
        "user": user,
    })