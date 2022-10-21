from flask import render_template, request, url_for, flash, redirect
from estimate_constructor.ns_works.utils import get_all_works, get_work
from estimate_constructor import app

@app.route('/works')
def works():
    works = get_all_works()
    return render_template('works.html', works=works)

@app.route('/constructor')
def constructor(work_id):
    work = get_work(work_id)
    return render_template('works.html', works=work)