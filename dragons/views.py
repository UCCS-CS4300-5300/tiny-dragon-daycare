from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Dragon


def home(request):
    dragon, _ = Dragon.objects.get_or_create(name='Puff', defaults={'hunger': 7})
    return render(request, 'dragons/home.html', {'dragon': dragon})


@require_POST
def feed_dragon(request, dragon_id):
    dragon = get_object_or_404(Dragon, id=dragon_id)
    dragon.feed()
    return redirect('home')
