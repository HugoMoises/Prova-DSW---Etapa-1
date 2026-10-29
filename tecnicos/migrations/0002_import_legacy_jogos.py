from django.db import migrations


def import_legacy_tecnicos(apps, schema_editor):
    connection = schema_editor.connection
    if 'jogos_tecnico' not in connection.introspection.table_names():
        return

    Tecnico = apps.get_model('tecnicos', 'Tecnico')
    Equipe = apps.get_model('equipes', 'Equipe')
    quote = connection.ops.quote_name
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, nome, email, telefone, equipe_id FROM {quote('jogos_tecnico')}"
        )
        rows = cursor.fetchall()

    equipe_ids = set(Equipe.objects.using(connection.alias).values_list('id', flat=True))
    Tecnico.objects.using(connection.alias).bulk_create(
        [
            Tecnico(id=row[0], nome=row[1], email=row[2], telefone=row[3], equipe_id=row[4])
            for row in rows if row[4] in equipe_ids
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ('equipes', '0002_import_legacy_jogos'),
        ('tecnicos', '0001_initial'),
    ]

    operations = [migrations.RunPython(import_legacy_tecnicos, migrations.RunPython.noop)]
