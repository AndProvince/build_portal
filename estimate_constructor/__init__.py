from flask import Flask
app = Flask(__name__)

import estimate_constructor.route
import estimate_constructor.ns_items.route
import estimate_constructor.ns_works.route

