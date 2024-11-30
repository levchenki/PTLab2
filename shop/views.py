import datetime

from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['birthdate'] = forms.DateField(
            required=True,
            widget=forms.DateInput(attrs={'type': 'date'}),
            label='Дата рождения'
        )
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)

        birthdate = form.cleaned_data.get('birthdate')
        self.object.final_cost = self.object.calculate_final_cost(birthdate)
        self.object.save()

        return HttpResponse(
            f'Спасибо за покупку, {self.object.person}! Итоговая стоимость: {self.object.final_cost} рублей.')
