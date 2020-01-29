# Generated by Django 2.2.2 on 2020-01-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0002_auto_20200126_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('Submit', 'Submit'), ('Review', 'Review'), ('Interview', 'Interview'), ('Hired', 'Hired')], default='Submit', max_length=10),
        ),
    ]
