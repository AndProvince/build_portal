from werkzeug.exceptions import abort
from estimate_constructor.model.utils import get_db_connection

def get_all_units():
    conn = get_db_connection()
    units = conn.execute('SELECT '
                         'UN.* '
                         'FROM unit AS UN').fetchall()
    conn.close()
    if units is None:
        abort(404)
    return units