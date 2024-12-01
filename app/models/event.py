#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from typing import Union

from . import db


class Event(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    event_type = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String)
    started_on = db.Column(db.DateTime, nullable=False)
    finished_on = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def __init__(
        self, event_type: str, title: str, started_on: str, finished_on: str,
        username: str, description: Union[None, str], url: Union[None, str]
    ) -> None:
        self.event_type = event_type
        self.title = title
        self.started_on = started_on
        self.finished_on = finished_on
        self.username = username

        if url:
            self.url = url
        if description:
            self.description = description

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"

    @staticmethod
    def get_user_monthly_events(username: str, date: str):
        date += '%'

        sql = db.text("""
            SELECT *
            FROM event
            WHERE username = :username
              AND TO_CHAR(created_on::TIMESTAMP, 'YYYY-MM-DD') LIKE :date
            ORDER BY created_on ASC;
        """)

        with db.engine.connect() as conn:
            result = conn.execute(
                sql, {'username': username, 'date': date}
            ).fetchall()

        return result
