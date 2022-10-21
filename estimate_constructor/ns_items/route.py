from flask import render_template, request, url_for, flash, redirect
from estimate_constructor.ns_items.utils import get_item, get_all_items
from estimate_constructor.ns_units.utils import get_all_units
from estimate_constructor.model.utils import get_db_connection
from estimate_constructor import app

@app.route('/items')
def items():
    items = get_all_items()
    return render_template('items.html', items=items)

@app.route('/items/<int:item_id>')
def item(item_id):
    item = get_item(item_id)
    return render_template('item.html', item=item)

@app.route('/items/create', methods=('GET', 'POST'))
def create():
    units = get_all_units()

    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        price = request.form['price']
        unit_id = request.form['unit']

        if not code or not name or not price:
            flash('Required all data!')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO items (code, name, price, unit_id) "
                         "VALUES (?, ?, ?, ?)",
                         (code, name, price, unit_id))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))

    return render_template('create.html', units=units)

@app.route('/items/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    item = get_item(id)
    units = get_all_units()

    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        price = request.form['price']
        unit_id = request.form['unit']


        if not code or not name or not price or not unit_id:
            flash('Required all data!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE items '
                         'SET code = ?, '
                         'name = ?, '
                         'price = ?, '
                         'unit_id = ? '
                         'WHERE id = ?',
                         (code, name, price, unit_id, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', item=item, units=units)

@app.route('/items/<int:id>/delete', methods=('POST',))
def delete(id):
    item = get_item(id)

    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    flash('"{}" was successfully deleted!'.format(item['name']))

    return redirect(url_for('index'))