# Generated by Django 3.2.18 on 2023-04-24 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choise',
            old_name='choise_text',
            new_name='choice_text',
        ),
    ]
