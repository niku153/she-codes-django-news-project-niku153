# Generated by Django 4.1.3 on 2022-12-12 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='newsstory',
            name='tags',
            field=models.CharField(default='untagged', max_length=200),
        ),
    ]