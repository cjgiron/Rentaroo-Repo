# Generated by Django 2.2.4 on 2021-07-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210721_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apartment_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]