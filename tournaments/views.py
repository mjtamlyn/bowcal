from django.utils import timezone
from django.views.generic import TemplateView

from .models import Tournament


class TournamentList(TemplateView):
    template_name = 'tournaments/tournament_list.html'

    def get_tournaments(self):
        return Tournament.objects.filter(
            end_date__gte=timezone.now().date
        ).select_related(
            'organising_club',
            'organising_county',
            'venue',
        ).prefetch_related('rounds').order_by(
            'start_date',
            'end_date',
        )

    def get_context_data(self, **kwargs):
        return {
            'tournaments': self.get_tournaments(),
        }
