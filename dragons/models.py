from django.db import models


class Dragon(models.Model):
    name = models.CharField(max_length=50, default='Puff')
    hunger = models.PositiveIntegerField(default=7)

    @property
    def mood(self):
        if self.hunger >= 7:
            return 'Grumpy'
        if self.hunger >= 3:
            return 'Content'
        return 'Happy'

    def feed(self):
        self.hunger = max(0, self.hunger - 2)
        self.save()

    def __str__(self):
        return self.name
