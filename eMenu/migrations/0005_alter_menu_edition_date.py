# Generated by Django 3.2 on 2021-05-05 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0004_alter_dish_edition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='edition_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]