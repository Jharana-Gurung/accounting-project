from django.shortcuts import render
from .models import Product, Sale, Purchase

def dashboard(request):
    total_sales = sum(s.total_price() for s in Sale.objects.all())
    total_purchases = sum(p.total_cost() for p in Purchase.objects.all())
    gross_profit = total_sales - total_purchases
    inventory_value = sum(p.quantity * p.cost_price for p in Product.objects.all())

    context = {
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'gross_profit': gross_profit,
        'inventory_value': inventory_value,
    }
    return render(request, "dashboard.html", context)
