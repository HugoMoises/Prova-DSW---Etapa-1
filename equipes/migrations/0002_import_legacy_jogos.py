from django.db import migrations


def import_legacy_equipes(apps, schema_editor):
    connection = schema_editor.connection
    if 'jogos_equipe' not in connection.introspection.table_names():
        return

    Equipe = apps.get_model('equipes', 'Equipe')
    quote = connection.ops.quote_name
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, nome, curso, cor, criada_em FROM {quote('jogos_equipe')}"
        )
        rows = cursor.fetchall()

    Equipe.objects.using(connection.alias).bulk_create(
        [Equipe(id=row[0], nome=row[1], curso=row[2], cor=row[3], criada_em=row[4]) for row in rows],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [('equipes', '0001_initial')]

    operations = [migrations.RunPython(import_legacy_equipes, migrations.RunPython.noop)]
