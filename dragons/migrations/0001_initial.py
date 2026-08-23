# Generated manually for the Tiny Dragon Daycare starter app.

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Puff', max_length=50)),
                ('hunger', models.PositiveIntegerField(default=7)),
            ],
        ),
    ]
