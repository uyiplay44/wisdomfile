# Generated by Django 4.0 on 2022-01-18 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Lead.user'),
        ),
    ]