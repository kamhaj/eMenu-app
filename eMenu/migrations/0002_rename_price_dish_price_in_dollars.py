# Generated by Django 3.2 on 2021-05-03 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='price',
            new_name='price_in_dollars',
        ),
    ]