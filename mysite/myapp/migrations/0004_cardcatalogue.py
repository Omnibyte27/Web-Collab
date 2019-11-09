# Generated by Django 2.2.5 on 2019-11-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_input_input2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardCatalogue',
            fields=[
                ('card_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('card_name', models.CharField(max_length=30)),
                ('top_value', models.IntegerField()),
                ('left_value', models.IntegerField()),
                ('right_value', models.IntegerField()),
                ('bottom_value', models.IntegerField()),
                ('times_card_played', models.IntegerField()),
            ],
        ),
    ]
