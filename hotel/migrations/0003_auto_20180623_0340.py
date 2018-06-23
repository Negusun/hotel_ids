# Generated by Django 2.0.6 on 2018-06-23 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20180623_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido_pat', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=150)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido_pat', models.CharField(max_length=60)),
                ('apellido_mat', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='hotel',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel'),
        ),
        migrations.AddField(
            model_name='acompanante',
            name='huesped',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Huesped'),
        ),
    ]