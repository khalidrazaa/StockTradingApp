from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Position

@login_required
def portfolio_view(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    positions = Position.objects.filter(portfolio=portfolio)
    return render(request, 'portfolio.html', {'positions': positions})

@login_required
def add_position(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        quantity = request.POST['quantity']
        purchase_price = request.POST['purchase_price']
        portfolio = Portfolio.objects.get_or_create(user=request.user)
        position = Position.objects.create(portfolio=portfolio, symbol=symbol, quantity=quantity, purchase_price=purchase_price)
        return redirect('portfolio')
    return render(request, 'add_position.html')

