#!/usr/bin/env python
# coding: utf-8
from flask import Blueprint
from flask_restful import Api
from .routes import PingAPI
from .routes.graphql import GraphQL

api_bp = Blueprint(name='api', import_name=__name__)

api = Api(api_bp)


api.add_resource(PingAPI, '/ping')
api.add_resource(GraphQL, '/graphql')
