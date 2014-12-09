from .models import Tournament


class TournamentAdapter(object):
    def get_list(self):
        return Tournament.objects.all()


tournaments = TournamentAdapter()
