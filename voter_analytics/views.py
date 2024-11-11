from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from . models import Voter
import plotly
import plotly.graph_objs as go
from django.db.models import Count
from django.db.models.functions import ExtractYear

# Create your views here.
class VotersListView(ListView):
    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        
        qs = super().get_queryset()

        # Filter by party affiliation
        party_affiliation = self.request.GET.get('party_affiliation')
        if party_affiliation:
            qs = qs.filter(party_affiliation=party_affiliation.strip())

        # Filter by minimum date of birth
        min_date_of_birth = self.request.GET.get('min_date_of_birth')
        if min_date_of_birth:
            qs = qs.filter(date_of_birth__year__gte=min_date_of_birth)

        # Filter by maximum date of birth
        max_date_of_birth = self.request.GET.get('max_date_of_birth')
        if max_date_of_birth:
            qs = qs.filter(date_of_birth__year__lte=max_date_of_birth)

        # Filter by voter score
        voter_score = self.request.GET.get('voter_score')
        if voter_score:
            qs = qs.filter(voter_score=int(voter_score))

        # Filter by election participation checkboxes
        if self.request.GET.get('v20state') == '1':
            qs = qs.filter(v20state=True)
        if self.request.GET.get('v21town') == '1':
            qs = qs.filter(v21town=True)
        if self.request.GET.get('v21primary') == '1':
            qs = qs.filter(v21primary=True)
        if self.request.GET.get('v22general') == '1':
            qs = qs.filter(v22general=True)
        if self.request.GET.get('v23town') == '1':
            qs = qs.filter(v23town=True)

       
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = list(range(1920, 2005))
        context['scores'] = list(range(0, 6))
        return context
    
class VoterDetailView(DetailView):

    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'v'

class GraphsView(ListView):
    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'voters'

    def get_queryset(self):
        
        qs = super().get_queryset()

        # Filter by party affiliation
        party_affiliation = self.request.GET.get('party_affiliation')
        if party_affiliation:
            qs = qs.filter(party_affiliation=party_affiliation.strip())

        # Filter by minimum date of birth
        min_date_of_birth = self.request.GET.get('min_date_of_birth')
        if min_date_of_birth:
            qs = qs.filter(date_of_birth__year__gte=min_date_of_birth)

        # Filter by maximum date of birth
        max_date_of_birth = self.request.GET.get('max_date_of_birth')
        if max_date_of_birth:
            qs = qs.filter(date_of_birth__year__lte=max_date_of_birth)

        # Filter by voter score
        voter_score = self.request.GET.get('voter_score')
        if voter_score:
            qs = qs.filter(voter_score=int(voter_score))

        # Filter by election participation checkboxes
        if self.request.GET.get('v20state') == '1':
            qs = qs.filter(v20state=True)
        if self.request.GET.get('v21town') == '1':
            qs = qs.filter(v21town=True)
        if self.request.GET.get('v21primary') == '1':
            qs = qs.filter(v21primary=True)
        if self.request.GET.get('v22general') == '1':
            qs = qs.filter(v22general=True)
        if self.request.GET.get('v23town') == '1':
            qs = qs.filter(v23town=True)

        
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()

        # Graph 1: Distribution of Voters by Year of Birth
        birth_years = voters.annotate(year_of_birth=ExtractYear('date_of_birth'))  # Extract year from date_of_birth
        year_counts = birth_years.values('year_of_birth').annotate(count=Count('id')).order_by('year_of_birth')
    
        x = [item['year_of_birth'] for item in year_counts]
        y = [item['count'] for item in year_counts]
        
        fig1 = go.Figure(data=[go.Bar(x=x, y=y)])
        fig1.update_layout(title_text="Voter Birth Year Distribution")
        context['birth_year_graph'] = plotly.offline.plot(fig1, auto_open=False, output_type="div")

        # Graph 2: Distribution of Voters by Party Affiliation
        party_counts = voters.values('party_affiliation').annotate(count=Count('id'))
        x = [item['party_affiliation'] for item in party_counts]
        y = [item['count'] for item in party_counts]
        
        fig2 = go.Figure(data=[go.Pie(labels=x, values=y)])
        fig2.update_layout(title_text="Voter Party Affiliation Distribution")
        context['party_affiliation_graph'] = plotly.offline.plot(fig2, auto_open=False, output_type="div")

        # Graph 3: Voter Participation in Each Election
        participation_counts = {
            '2020 State': voters.filter(v20state=True).count(),
            '2021 Town': voters.filter(v21town=True).count(),
            '2021 Primary': voters.filter(v21primary=True).count(),
            '2022 General': voters.filter(v22general=True).count(),
            '2023 Town': voters.filter(v23town=True).count(),
        }
        x, y = zip(*participation_counts.items())

        fig3 = go.Figure(data=[go.Bar(x=x, y=y)])
        fig3.update_layout(title_text="Voter Participation in Elections")
        context['election_participation_graph'] = plotly.offline.plot(fig3, auto_open=False, output_type="div")

        
        context['years'] = list(range(1900, 2005))
        context['scores'] = list(range(0, 6))

        return context