# Generated by Django 3.2.9 on 2021-11-27 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_message_task_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.message', verbose_name='parent'),
        ),
    ]
