from django import forms

from .models import Tournament


class TournamentSubmissionForm(forms.ModelForm):
    multi_day_shoot = forms.BooleanField(required=False)

    class Meta:
        model = Tournament
        fields = (
            'name',
            'start_date',
            'end_date',
            'organising_club',
            'organising_county',
            'series',
            'venue',
            'shoot_type',
            'record_status',
            'rounds',
            'submission_notes',
        )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['end_date'].required = False

    def clean(self):
        if self.cleaned_data.get('multi_day_shoot') and not self.cleaned_data.get('end_date'):
            self.add_error('end_date', self.fields['end_date'].error_messages['required'])

    def save(self, **kwargs):
        if not self.cleaned_data['multi_day_shoot']:
            self.instance.end_date = self.instance.start_date
        return super().save(**kwargs)
