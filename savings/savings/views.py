from django.shortcuts import render,redirect
from django.views import View
from .models import SavingCalc


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'savings/dashboard.html')

    def post(self, pk, request, *args, **kwargs):
        day = request.POST.get("day")
        month = request.POST.get("month")
        is_paid = request.POST.get("paid")
        saved = SavingCalc.objects.creae(
            day=day,
            month=month,
            is_paid=is_paid,
        )
        saved.object.get(pk=pk )
        saved.is_paid = True
        saved.save()

        context = {
            'saved': saved
        }

        return redirect('savings_details')


class SavingDetail(View):
    def get(self,request, pk, *args, **kwargs):
        saved = SavingCalc.objects.get(pk=pk)
        context={
            'saved': saved
        }

        return render(request, 'savings/savings_details.html', context)