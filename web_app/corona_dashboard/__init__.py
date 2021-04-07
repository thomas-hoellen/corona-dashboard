from flask import Flask

app = Flask(__name__)

from corona_dashboard import routes
