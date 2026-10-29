from django.db import migrations


def import_legacy_atletas(apps, schema_editor):
    connection = schema_editor.connection
    tables = set(connection.introspection.table_names())
    if 'jogos_atleta' not in tables:
        return

    Atleta = apps.get_model('atletas', 'Atleta')
    Equipe = apps.get_model('equipes', 'Equipe')
    Modalidade = apps.get_model('modalidades', 'Modalidade')
    quote = connection.ops.quote_name
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, nome, matricula, data_nascimento, equipe_id "
            f"FROM {quote('jogos_atleta')}"
        )
        atleta_rows = cursor.fetchall()

    equipe_ids = set(Equipe.objects.using(connection.alias).values_list('id', flat=True))
    Atleta.objects.using(connection.alias).bulk_create(
        [
            Atleta(
                id=row[0], nome=row[1], matricula=row[2],
                data_nascimento=row[3], equipe_id=row[4],
            )
            for row in atleta_rows if row[4] in equipe_ids
        ],
        ignore_conflicts=True,
    )

    through = Atleta.modalidade.through
    atleta_ids = set(Atleta.objects.using(connection.alias).values_list('id', flat=True))
    modalidade_ids = set(Modalidade.objects.using(connection.alias).values_list('id', flat=True))
    if 'jogos_atleta_modalidade' not in tables:
        return

    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT atleta_id, modalidade_id FROM {quote('jogos_atleta_modalidade')}"
        )
        links = cursor.fetchall()

    through.objects.using(connection.alias).bulk_create(
        [
            through(atleta_id=atleta_id, modalidade_id=modalidade_id)
            for atleta_id, modalidade_id in links
            if atleta_id in atleta_ids and modalidade_id in modalidade_ids
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ('atletas', '0001_initial'),
        ('equipes', '0002_import_legacy_jogos'),
        ('modalidades', '0003_import_legacy_jogos'),
    ]

    operations = [migrations.RunPython(import_legacy_atletas, migrations.RunPython.noop)]
