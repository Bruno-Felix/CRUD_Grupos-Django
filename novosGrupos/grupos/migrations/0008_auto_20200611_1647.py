# Generated by Django 3.0.7 on 2020-06-11 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0007_auto_20200611_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Artista')),
                ('idade', models.PositiveIntegerField(verbose_name='Idade do Artista')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2, verbose_name='Gênero do Artista')),
                ('pais', models.CharField(max_length=100, verbose_name='País do Artista')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Foto do Artista')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo', verbose_name='Grupo do Artista')),
            ],
        ),
        migrations.AlterField(
            model_name='comeback',
            name='data',
            field=models.DateField(verbose_name='Data do Música'),
        ),
        migrations.AlterField(
            model_name='comeback',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo', verbose_name='Grupo do Artista'),
        ),
        migrations.DeleteModel(
            name='Integrante',
        ),
    ]
