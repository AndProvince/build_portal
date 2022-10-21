from werkzeug.exceptions import abort
from estimate_constructor.model.utils import get_db_connection

def get_all_works():
    conn = get_db_connection()
    works = conn.execute('SELECT '
                         'WR.*, '
                         'UN.name AS unit '
                         'FROM works AS WR '
                         'LEFT JOIN unit AS UN ON UN.id = WR.unit_id').fetchall()
    conn.close()
    if works is None:
        abort(404)
    return works

def get_work(work_id):
    conn = get_db_connection()
    work = conn.execute('SELECT WR.*, '
                        'UN.name AS unit '
                        'FROM works AS WR '
                        'JOIN unit AS UN ON UN.id = WR.unit_id '
                        'WHERE WR.id = ?',
                        (work_id,)).fetchone()
    conn.close()
    if work is None:
        abort(404)
    return work