# Generated by Django 4.2.1 on 2023-05-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='save_info',
            name='Address',
            field=models.CharField(default=[21.443173790181575, 105.85665111237604], max_length=40),
            preserve_default=False,
        ),
    ]
