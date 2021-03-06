# Generated by Django 2.0.13 on 2020-01-19 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Area'),
        ),
    ]
