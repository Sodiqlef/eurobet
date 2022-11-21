from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bet, Club
from  django.db.models import Q

# Create your views here.




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
    d1 = Bet.objects.filter(played=False).filter(competition="Division 1 League").first()
    d2 = Bet.objects.filter(played=False).filter(competition="Division 2 League").first()
    d1c = Bet.objects.filter(played=False).filter(competition="League Cup, Division 1").first()
    d2c = Bet.objects.filter(played=False).filter(competition="League Cup, Division 2").first()
    cl = Bet.objects.filter(played=False).filter(competition="Champions League").first()
    el = Bet.objects.filter(played=False).filter(competition="Europa League").first()
    sc = Bet.objects.filter(played=False).filter(competition="Super Cup").first()
    im = Bet.objects.filter(played=False).filter(competition="International Match").first()
    bets = Bet.objects.filter(played=False).order_by('-date')
    return render(request, 'index.html', {'bets': bets, 'd1': d1, 'd2': d2, 'd1c': d1c,
                                            'd2c': d2c, 'cl': cl, 'el': el, 'sc': sc, 'im': im})

def result(request):
    
    search = request.GET.get('match')
    if search:
        queryset = Bet.objects.filter(Q(home_name__name__icontains=search)).order_by('-date')
        bets = paging(25, queryset, request)
    else:
        queryset = Bet.objects.all().order_by('-date')
        bets = paging(20, queryset, request)
    return render(request, 'result.html', {'bets': bets})