from django import forms


class CounterAttackForm(forms.Form):
    card = forms.IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, offered_cards=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.offered_cards = offered_cards or []

    def clean_card(self):
        card = self.cleaned_data["card"]
        if self.offered_cards and card not in self.offered_cards:
            raise forms.ValidationError("제공된 카드 5장 중 하나를 선택해야 합니다.")
        return card
