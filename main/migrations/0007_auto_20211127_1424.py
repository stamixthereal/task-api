# Generated by Django 3.2.9 on 2021-11-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_task_to_message_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
