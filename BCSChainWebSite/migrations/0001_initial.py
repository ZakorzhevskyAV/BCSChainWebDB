# Generated by Django 3.2.5 on 2021-07-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('height', models.IntegerField(primary_key=True, serialize=False, verbose_name='height')),
                ('hash', models.CharField(max_length=50, verbose_name='hash')),
                ('timestamp', models.IntegerField(verbose_name='timestamp')),
                ('miner', models.CharField(max_length=50, verbose_name='miner')),
                ('transactions_num', models.IntegerField(verbose_name='transactions_num')),
            ],
            options={
                'ordering': ('height',),
            },
        ),
    ]
