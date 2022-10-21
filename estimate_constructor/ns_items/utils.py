from werkzeug.exceptions import abort
from estimate_constructor.model.utils import get_db_connection

def get_all_items():
    conn = get_db_connection()
    items = conn.execute('SELECT '
                         'IT.*, '
                         'UN.name AS unit '
                         'FROM items AS IT '
                         'LEFT JOIN unit AS UN ON UN.id = IT.unit_id').fetchall()
    conn.close()
    if items is None:
        abort(404)
    return items

def get_item(item_id):
    conn = get_db_connection()
    item = conn.execute('SELECT IT.*, '
                        'UN.name AS unit '
                        'FROM items AS IT '
                        'JOIN unit AS UN ON UN.id = IT.unit_id '
                        'WHERE IT.id = ?',
                        (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item
