from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    from core.forms import SignupForm
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    values = {"items": items, "categories": categories}
    return render(request, 'core/index.html', values)


def contact(request):
    return render(request, 'core/contact.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })