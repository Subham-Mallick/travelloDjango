# Generated by Django 2.2.3 on 2019-07-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='page',
            field=models.CharField(default='place.html', max_length=5000),
            preserve_default=False,
        ),
    ]