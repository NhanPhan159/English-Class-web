# Generated by Django 4.1 on 2022-08-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='grade',
            field=models.CharField(choices=[('1', 'Lớp 1'), ('2', 'Lớp 2'), ('3', 'Lớp 3'), ('4', 'Lớp 4'), ('5', 'Lớp 5'), ('6', 'Lớp 6'), ('7', 'Lớp 7'), ('8', 'Lớp 8'), ('9', 'Lớp 9'), ('10', 'Lớp 10'), ('11', 'Lớp 11'), ('12', 'Lớp 12')], default='10', max_length=2),
        ),
    ]
