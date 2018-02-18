from flask import Flask, request, render_template
import os

app = Flask(__name__)
static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client")

app = AppStarter()
app.register_routes_to_resources(static_folder_root)
app.run(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('Website.html', name=name)
