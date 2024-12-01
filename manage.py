#!/usr/bin/env python
# coding: utf-8
import os
import sys

from flask_migrate import Migrate

from app.app import create_api_app
from app.models import db


MODE = str(sys.argv[1])
config_name = os.getenv('ENV_MODE') or 'dev'

app = create_api_app(config_name)
migrate = Migrate(app, db, compare_type=True)

match MODE:
    case "api":
        app.run(
            use_debugger=app.config['DEBUG'],
            use_reloader=True,
            host=app.config['HOST'],
            port=app.config['API_PORT']
        )
    case _:
        pass
