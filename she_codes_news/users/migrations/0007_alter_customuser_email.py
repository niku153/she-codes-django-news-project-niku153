# Generated by Django 4.1.3 on 2022-12-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
    ]
