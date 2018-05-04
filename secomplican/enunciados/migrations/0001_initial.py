# Generated by Django 2.0.5 on 2018-05-04 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConjuntoDeEnunciados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cuatrimestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('cuatrimestre', models.IntegerField(choices=[(1, 'Primer Cuatrimestre'), (2, 'Segundo Cuatrimestre'), (3, 'Verano')])),
            ],
        ),
        migrations.CreateModel(
            name='Enunciado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='Solucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('enunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.Enunciado')),
            ],
        ),
        migrations.CreateModel(
            name='Parcial',
            fields=[
                ('conjuntodeenunciados_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enunciados.ConjuntoDeEnunciados')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField(blank=True, null=True)),
                ('recuperatorio', models.BooleanField(default=False)),
            ],
            bases=('enunciados.conjuntodeenunciados',),
        ),
        migrations.CreateModel(
            name='Practica',
            fields=[
                ('conjuntodeenunciados_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enunciados.ConjuntoDeEnunciados')),
                ('numero', models.IntegerField()),
                ('titulo', models.CharField(default='', max_length=1023)),
            ],
            bases=('enunciados.conjuntodeenunciados',),
        ),
        migrations.AddField(
            model_name='enunciado',
            name='conjunto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.ConjuntoDeEnunciados'),
        ),
        migrations.AddField(
            model_name='conjuntodeenunciados',
            name='cuatrimestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.Cuatrimestre'),
        ),
        migrations.AddField(
            model_name='conjuntodeenunciados',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.Materia'),
        ),
    ]
