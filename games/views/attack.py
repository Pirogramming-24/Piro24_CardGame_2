import random
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..models import Game

User = get_user_model()

@login_required
def attack(request):
    """
    공격하기 페이지 (카드 선택 + 상대 선택)
    GET: 랜덤 카드 5장 제공
    POST: 게임 생성 및 DB 저장
    """
    session_key = "attack_cards"
    
    if request.method == "GET":
        # 1~10 중 랜덤으로 5장 선택
        cards = random.sample(range(1, 11), 5)
        request.session[session_key] = cards
        
        # 자신을 제외한 다른 유저 목록
        other_users = User.objects.exclude(id=request.user.id)
        
        return render(request, "games/attack.html", {
            "cards": cards,
            "other_users": other_users,
        })
    
    # POST: 게임 생성
    cards = request.session.get(session_key, [])
    selected_card = int(request.POST.get("card"))
    defender_id = int(request.POST.get("defender"))
    
    # 유효성 검사
    if selected_card not in cards:
        return redirect("games:attack")
    
    defender = User.objects.get(id=defender_id)
    
    # 게임 생성
    game = Game.objects.create(
        attacker=request.user,
        defender=defender,
        attacker_card=selected_card,
        status=Game.Status.PENDING,
    )
    
    # 세션 카드 정보 삭제
    request.session.pop(session_key, None)
    
    # 생성된 게임 상세 페이지로 이동
    return redirect("games:detail", pk=game.id)