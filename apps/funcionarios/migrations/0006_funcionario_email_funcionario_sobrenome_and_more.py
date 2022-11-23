# Generated by Django 4.0.2 on 2022-02-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_alter_funcionario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='email',
            field=models.CharField(default=1, help_text='E-mail', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='sobrenome',
            field=models.CharField(default=1, help_text='Sobre nome do funcionario', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='telefone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]