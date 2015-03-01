from django import forms

from .models import Tournament


class TournamentSubmissionForm(forms.ModelForm):
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
