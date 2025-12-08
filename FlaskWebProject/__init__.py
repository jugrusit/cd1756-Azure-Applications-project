# FlaskWebProject/__init__.py
"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# NEW: import ProxyFix
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config.from_object(Config)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)
app.logger.setLevel(logging.INFO)
app.logger.info("Article CMS app initialized.")

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# NEW: Make Flask honor reverse proxy headers so it recognizes HTTPS correctly.
# Trust one hop of X-Forwarded-For, X-Forwarded-Proto, and X-Forwarded-Host.
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

# NEW (optional but helpful): prefer https when building external URLs
app.config['PREFERRED_URL_SCHEME'] = 'https'

import FlaskWebProject.views

