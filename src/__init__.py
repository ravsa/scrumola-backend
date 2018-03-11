#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for
from flask_appconfig import AppConfig


def create_app(configfile=None):
    from .api_v1 import app_v1

    app = Flask(__name__)
    AppConfig(app, configfile)
    app.register_blueprint(app_v1)

    @app.route('/')
    def base_url():
        return redirect(url_for('api_v1.apiendpoints__slashless'))

    return app


app = create_app()
