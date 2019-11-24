# Generated by Django 2.2.5 on 2019-11-21 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='card1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card1create', to='myapp.CardCatalogue'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='card2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card2create', to='myapp.CardCatalogue'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='card3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card3create', to='myapp.CardCatalogue'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='card4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card4create', to='myapp.CardCatalogue'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='card5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card5create', to='myapp.CardCatalogue'),
        ),
    ]