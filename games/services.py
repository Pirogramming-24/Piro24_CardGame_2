import random
from django.db import transaction
from django.utils import timezone

from .models import Game, PlayerScore

@transaction.atomic
def resolve_game(game_id, defender_user, defender_card):
    game = Game.objects.select_for_update().get(pk=game_id)

    rule = random.choice([
        Game.Rule.BIGGER_WINS,
        Game.Rule.SMALLER_WINS,
    ])

    if game.attacker_card == defender_card:
        winner = Game.Winner.DRAW
        a_delta = d_delta = 0
    else:
        attacker_win = (
            game.attacker_card > defender_card
            if rule == Game.Rule.BIGGER_WINS
            else game.attacker_card < defender_card
        )
        if attacker_win:
            winner = Game.Winner.ATTACKER
            a_delta = game.attacker_card
            d_delta = -defender_card
        else:
            winner = Game.Winner.DEFENDER
            a_delta = -game.attacker_card
            d_delta = defender_card

    game.defender_card = defender_card
    game.rule = rule
    game.winner = winner
    game.attacker_delta = a_delta
    game.defender_delta = d_delta
    game.status = Game.Status.FINISHED
    game.resolved_at = timezone.now()
    game.save()

    a_score, _ = PlayerScore.objects.get_or_create(user=game.attacker)
    d_score, _ = PlayerScore.objects.get_or_create(user=game.defender)

    a_score.score += a_delta
    d_score.score += d_delta
    a_score.save()
    d_score.save()
