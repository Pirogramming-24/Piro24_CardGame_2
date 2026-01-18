from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import PlayerScore


@login_required
def ranking(request):
    rankings = PlayerScore.objects.select_related("user").order_by("-score")
    return render(request, "games/ranking.html", {
        "rankings": rankings
    })
