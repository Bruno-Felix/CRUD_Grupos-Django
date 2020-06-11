# Generated by Django 3.0.7 on 2020-06-11 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0006_grupo_integrante'),
    ]

    operations = [
        migrations.AddField(
            model_name='comeback',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='integrante',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
            preserve_default=False,
        ),
    ]