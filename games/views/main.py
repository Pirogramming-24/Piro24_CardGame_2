from django.shortcuts import render, redirect

def main(request):
    """
    메인 페이지
    - 로그인 전: 로그인/회원가입 버튼
    - 로그인 후: 유저 정보 + 게임 시작 버튼
    """
    if not request.user.is_authenticated:
        return render(request, "games/main_logout.html")
    
    return render(request, "games/main.html", {
        "user": request.user
    })