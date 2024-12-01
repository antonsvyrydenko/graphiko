#!/usr/bin/env python
# coding: utf-8
from loguru import logger

from flask_restful import Resource


class PingAPI(Resource):
    @staticmethod
    def get():
        logger.debug("/ping")
        # a simple endpoint to check status of service
        return {"success": True}, 200
