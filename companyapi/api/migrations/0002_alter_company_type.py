# Generated by Django 4.1 on 2023-06-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobiles Phones', 'Mobile Phones')], max_length=100),
        ),
    ]