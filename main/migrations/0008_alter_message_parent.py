# Generated by Django 3.2.9 on 2021-11-27 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211127_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='main.message', verbose_name='parent'),
        ),
    ]
