# Generated by Django 5.1 on 2024-08-14 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
