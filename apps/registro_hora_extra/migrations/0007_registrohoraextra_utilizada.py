# Generated by Django 4.0.4 on 2022-11-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0006_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]