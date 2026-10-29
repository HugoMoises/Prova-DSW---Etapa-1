from django.db import migrations


def import_legacy_modalidades(apps, schema_editor):
    connection = schema_editor.connection
    if 'jogos_modalidade' not in connection.introspection.table_names():
        return

    Modalidade = apps.get_model('modalidades', 'Modalidade')
    quote = connection.ops.quote_name
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, nome, tipo, max_atletas FROM {quote('jogos_modalidade')}"
        )
        rows = cursor.fetchall()

    tipo_atual = {'coletiva': 'C', 'individual': 'I', 'C': 'C', 'I': 'I'}
    Modalidade.objects.using(connection.alias).bulk_create(
        [
            Modalidade(
                id=row[0], nome=row[1], tipo=tipo_atual.get(row[2], row[2]),
                max_atletas=row[3],
            )
            for row in rows
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [('modalidades', '0002_alter_modalidade_tipo')]

    operations = [migrations.RunPython(import_legacy_modalidades, migrations.RunPython.noop)]
