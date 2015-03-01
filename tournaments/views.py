from django.views.generic import TemplateView

from .models import Tournament


class TournamentList(TemplateView):
    template_name = 'tournaments/tournament_list.html'

    def get_tournaments(self):
        return Tournament.objects.all()

    def get_context_data(self, **kwargs):
        return {
            'tournaments': self.get_tournaments(),
        }
