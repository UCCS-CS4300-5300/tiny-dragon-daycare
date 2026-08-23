import pytest

from .models import Dragon


@pytest.mark.django_db
def test_feeding_reduces_hunger():
    dragon = Dragon.objects.create(name='Puff', hunger=7)

    dragon.feed()

    assert dragon.hunger == 5


@pytest.mark.django_db
def test_hunger_cannot_go_below_zero():
    dragon = Dragon.objects.create(name='Puff', hunger=1)

    dragon.feed()

    assert dragon.hunger == 0
