#!/usr/bin/env python
# coding: utf-8
from loguru import logger

from ariadne import (
    load_schema_from_path, make_executable_schema, graphql_sync,
    snake_case_fallback_resolvers, ObjectType
)

from flask import request, jsonify
from flask_restful import Resource

from ..utils.resolvers import (
    get_user_events_resolver, get_user_monthly_events_resolver,
    post_event_resolver, update_event_resolver, delete_event_resolver
)


query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("getUserEvents", get_user_events_resolver)
query.set_field("getUserMonthlyEvents", get_user_monthly_events_resolver)

mutation.set_field("createEvent", post_event_resolver)
mutation.set_field("updateEvent", update_event_resolver)
mutation.set_field("deleteEvent", delete_event_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


class GraphQL(Resource):
    @staticmethod
    def post():
        logger.debug("/graphql")

        data = request.get_json()
        success, result = graphql_sync(
            schema, data, context_value=request, debug=True
        )
        status_code = 200 if success else 400

        response = jsonify(data)
        response.status_code = status_code

        return jsonify(result)
