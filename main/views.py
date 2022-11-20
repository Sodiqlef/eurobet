from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bet, Club

# Create your views here.


d1 = Bet.objects.filter(played=False).filter(competition="Division 1 League")
d2 = Bet.objects.filter(played=False).filter(competition="Division 2 League")
d1c = Bet.objects.filter(played=False).filter(competition="League Cup, Division 1")
d2c = Bet.objects.filter(played=False).filter(competition="League Cup, Division 2")
cl = Bet.objects.filter(played=False).filter(competition="Champions League")
el = Bet.objects.filter(played=False).filter(competition="Europa League")
sc = Bet.objects.filter(played=False).filter(competition="Super Cup")
im = Bet.objects.filter(played=False).filter(competition="International Match")

def paging(val, queryset, request):
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, val)
    try:
        bets = paginator.page(page)
    except PageNotAnInteger:

        bets = paginator.page(1)
    except EmptyPage:
        bets = paginator.page(paginator.num_pages)

    return bets

def home(request):
    bets = Bet.objects.filter(played=False).order_by('-date')
    return render(request, 'index.html', {'bets': bets, 'd1': d1, 'd2': d2, 'd1c': d1c,
                                            'd2c': d2c, 'cl': cl, 'el': el, 'sc': sc, 'im': im})

def result(request):
    queryset = Bet.objects.all().filter(played=True).order_by('-date')
    bets = paging(25, queryset, request)
    return render(request, 'expand.html', {'bets': bets})