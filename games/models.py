from __future__ import annotations

from django.conf import settings
from django.db import models


class PlayerScore(models.Model):
    """
    유저 누적 점수 (랭킹 기준) - 유저별 누적 점수로 정렬 :contentReference[oaicite:2]{index=2}
    accounts를 건드리지 않기 위해 games 앱에 둠.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="player_score")
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user} ({self.score})"


class Game(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        FINISHED = "FINISHED", "Finished"

    class Rule(models.TextChoices):
        BIGGER_WINS = "BIGGER_WINS", "Bigger wins"
        SMALLER_WINS = "SMALLER_WINS", "Smaller wins"

    class Winner(models.TextChoices):
        ATTACKER = "ATTACKER", "Attacker"
        DEFENDER = "DEFENDER", "Defender"
        DRAW = "DRAW", "Draw"

    attacker = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="games_attacked"
    )
    defender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="games_defended"
    )

    attacker_card = models.PositiveSmallIntegerField(null=True, blank=True)
    defender_card = models.PositiveSmallIntegerField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    rule = models.CharField(max_length=20, choices=Rule.choices, null=True, blank=True)
    winner = models.CharField(max_length=10, choices=Winner.choices, null=True, blank=True)

    attacker_delta = models.IntegerField(default=0)
    defender_delta = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Game#{self.pk} {self.attacker} vs {self.defender} [{self.status}]"

    def is_participant(self, user) -> bool:
        return user == self.attacker or user == self.defender
