from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from ..models import Game

@login_required
def delete_game(request, pk):
    """
    게임 취소 기능
    - 본인이 공격한 게임만 삭제 가능
    - 반격 전(PENDING 상태)만 삭제 가능
    """
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return redirect("games:list")
    
    # 본인이 공격자인지 확인
    if request.user != game.attacker and not request.user.is_superuser:
        return redirect("games:list")
    
    # PENDING 상태인지 확인
    if game.status != Game.Status.PENDING:
        return redirect("games:list")
    
    # 게임 삭제
    game.delete()
    
    return redirect("games:list")