# Generated by Django 4.1 on 2023-06-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_company_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('IT', 'IT'), ('NON-IT', 'NOT-IT'), ('MOBILE PHONE', 'MOBILE PHONE')], max_length=100),
        ),
    ]