import json
from datetime import date, timedelta

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView

from leagues.forms import LeagueForm
from leagues.models import League, Team, Draft, Matchup
from players.models import Player, Quote
from schedule.models import Season, Game, StatLine


class BDLView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(BDLView, self).get_context_data(*args, **kwargs)
        quote = Quote.objects.order_by('?').first()
        context["quote"] = quote
        return context


class HomePageView(BDLView):
    template = "site_base.html"

    def top_performers(self, day):
        games = Game.objects.filter(date=day)
        statlines = list(StatLine.objects.filter(game__in=games))
        statlines.sort(key=lambda x: x.game_score, reverse=True)
        return statlines[:8] # grab the 4 best performances

    def goat_performances(self):
        season = Season.objects.last()
        games = Game.objects.filter(season=season, date__lt=date.today())
        statlines = list(StatLine.objects.filter(game__in=games))
        statlines.sort(key=lambda x: x.game_score, reverse=True)
        return statlines[:20]

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        
        yesterday = date.today() - timedelta(days=1)
        yesterdays_best = self.top_performers(yesterday)
        if not yesterdays_best:
            yesterday = date.today() - timedelta(days=2)
            yesterdays_best = self.top_performers(yesterday)

        context["leagues"] = League.objects.filter(is_public=True) 
        context["yesterday"] = yesterday.strftime("%A, %B %-d")
        context["yesterdays_best"] = yesterdays_best
        context["season_best"] = self.goat_performances()
        return context


class LeagueView(BDLView):
    template_name = "league.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.league = League.objects.get(id=kwargs['league_id'])
        return super(LeagueView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(LeagueView, self).get_context_data(*args, **kwargs)
        
        league = League.objects.get(id=kwargs['league_id'])
        league_data = league.to_data()

        context["league_data"] = league_data
        return context


class CreateLeagueView(FormView):
    template_name = 'create_league.html'
    form_class = LeagueForm

    def form_valid(self, form):
        form.create_league()
        league = League.objects.last()
        redirect_url = reverse('league', kwargs={'league_id': league.id})
        return redirect(redirect_url)


class TeamView(LeagueView):
    template_name = "team.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TeamView, self).get_context_data(*args, **kwargs)
        
        team = Team.objects.get(id=kwargs['team_id'])
        team_data = team.to_data(player_data=True)

        context["team_data"] = team_data
        return context


class MatchupView(LeagueView):
    template_name = 'matchup.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MatchupView, self).get_context_data(*args, **kwargs)
        matchup = Matchup.objects.get(id=kwargs['matchup_id'])
        context["matchup_data"] = matchup.to_data()
        return context


class FreeAgentsView(LeagueView):
    template_name = "free_agents.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FreeAgentsView, self).get_context_data(*args, **kwargs)
        
        players = [p for p in Player.objects.filter(rostered=True) if p.is_available(league_id=self.league.id) and p.season_form != 0]
        player_data = [player.to_data() for player in players]

        context["player_data"] = player_data
        return context


class DraftResultsView(LeagueView):
    template_name = "draft/draft_results.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DraftResultsView, self).get_context_data(*args, **kwargs)
        
        draft = Draft.objects.get(league=self.league)
        draft_data = draft.to_data()

        context["draft_data"] = draft_data
        return context


