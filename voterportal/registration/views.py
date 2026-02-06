from django.shortcuts import render, get_object_or_404, redirect
from .models import Voter
from .forms import VoterForm

def voter_list(request):
    voters = Voter.objects.all()
    return render(request, 'registration/voter_list.html', {'voters': voters})

def voter_create(request):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voter_list')
    else:
        form = VoterForm()
    return render(request, 'registration/voter_form.html', {'form': form})

def voter_update(request, pk):
    voter = get_object_or_404(Voter, pk=pk)
    if request.method == 'POST':
        form = VoterForm(request.POST, instance=voter)
        if form.is_valid():
            form.save()
            return redirect('voter_list')
    else:
        form = VoterForm(instance=voter)
    return render(request, 'registration/voter_form.html', {'form': form})

def voter_delete(request, pk):
    voter = get_object_or_404(Voter, pk=pk)
    if request.method == 'POST':
        voter.delete()
        return redirect('voter_list')
    return render(request, 'registration/voter_confirm_delete.html', {'voter': voter})

def voter_detail(request, pk):
    voter = get_object_or_404(Voter, pk=pk)
    return render(request, 'registration/voter_detail.html', {'voter': voter})

from django.db.models import Q

def voter_search(request):
    query = request.GET.get('q')
    print(query,'line no 43')
    voter = None
    if query:
        try:
            voter = Voter.objects.get(Q(voter_id=query) | Q(first_name=query))
        except Voter.DoesNotExist:
            voter = None
    return render(request, 'registration/voter_search.html', {'voter': voter, 'query': query})