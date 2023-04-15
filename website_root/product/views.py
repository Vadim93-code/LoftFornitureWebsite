from django.shortcuts import render
from .models import Product
from .mail_form import EmailForm


def index_page(request):
    item = Product.objects.all()

    return render(request, './index.html', {'item': item})


def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()

    form = EmailForm()
    context = {
        "form": form
    }
    return render(request, './contact.html', context)
