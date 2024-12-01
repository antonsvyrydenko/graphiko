#!/usr/bin/env python
# coding: utf-8
import configparser

from flask import Flask


class Config:
    def __init__(self) -> None:
        path = 'conf/config.conf'
        self.parser = configparser.ConfigParser()
        self.parser.read(path)

    def _load_settings(
            self, app: Flask, required_section: str = 'common') -> Flask:
        for key, value in self.parser[required_section].items():
            app.config[key.upper()] = value

        return app

    def get_config(self, app: Flask, required_conf: str) -> Flask:
        # first we load common settings
        app = self._load_settings(app)

        # finally we load required settings based on env
        app = self._load_settings(app, required_conf)

        return app
