from django.shortcuts import render, redirect
from django.views import View
from .models import SavingCalc
from django.utils.timezone import datetime

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        saved = SavingCalc.objects.all()
        context = {
            'saved': saved
        }
        return render(request, 'savings/dashboard.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        day = request.POST.get("day")
        month = request.POST.get("month")
        price = request.POST.get("price")
        category = request.POST.get("category")
        now = datetime.now()
        th = int(now.strftime("%H"))
        tm = int(now.strftime("%M"))
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            saved = SavingCalc.objects.get(pk__contains=(int(item),))
            item_data = {
                'id': saved.pk,
                'name': saved.name,
                'price': saved.price
            }
            order_items['items'].append(item_data)

        saved = SavingCalc.objects.create(
            day=day,
            month=month,
            name=name,
            price=price,
            category=category,
            time_hour=th,
            time_min=tm
        )

        saved.is_paid = True
        saved.save()

        context = {
            'saved': saved
        }

        return redirect('savings_details', pk=saved.pk)


class SavingDetail(View):
    def get(self, request, pk, *args, **kwargs):
        saved = SavingCalc.objects.get(pk=pk)
        context = {
            'pk': saved.pk,
            'saved': saved
        }

        return render(request, 'savings/savings_details.html', context)


class History(View):
    def get(self, request, *args, **kwargs):
        saved = SavingCalc.objects.all()
        price = 0
        all_savings = []
        for save in saved:
            price += save.price
            all_savings.append(save)

        context = {
            'saves': all_savings,
            'total_save': len(saved),
            'total_savings': price
        }
        return render(request, 'savings/history.html', context)
