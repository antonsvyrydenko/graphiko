#!/usr/bin/env python
# coding: utf-8
from ariadne import convert_kwargs_to_snake_case

from loguru import logger

from app.models.event import Event
from app.models import db


@convert_kwargs_to_snake_case
def get_user_events_resolver(*args, **kwargs):

    username = kwargs['username']
    logger.debug(f'get user events: {username}')

    events = list(Event.query.filter_by(username=username).all())
    if events:
        return {
            "success": True,
            "event": events
        }

    return {
        "success": False,
        "errors": [f"events for username {username} not found"]
    }


@convert_kwargs_to_snake_case
def get_user_monthly_events_resolver(*args, **kwargs):

    username = kwargs['username']
    date = kwargs['date']
    logger.debug(f'get user monthly events: {username}, {date}')

    events = list(Event.get_user_monthly_events(username, date))
    if events:
        return {
            "success": True,
            "event": events
        }

    return {
        "success": False,
        "errors": [
            f"events for username '{username}' by date '{date}' not found"
        ]
    }


@convert_kwargs_to_snake_case
def post_event_resolver(*args, **kwargs):

    new_event = Event(
        event_type=kwargs['event_type'], title=kwargs['title'],
        started_on=kwargs['started_on'], finished_on=kwargs['finished_on'],
        username=kwargs['username'], url=kwargs.get('url'),
        description=kwargs.get('description')
    )
    logger.debug(f'post event: {new_event}')

    db.session.add(new_event)
    db.session.commit()

    payload = {
        "success": True,
        "event": new_event
    }

    return payload

@convert_kwargs_to_snake_case
def update_event_resolver(*args, **kwargs):

    event = Event.query.filter_by(id=kwargs['id']).first()
    logger.debug(f'update event: {event}')

    if not event:
        payload = {
            "success": False,
            "errors": [f"Not found event with id: {kwargs['id']}"]
        }

    else:
        # update event with values present in kwargs
        for key, value in kwargs.items():
            setattr(event, key, value)

        logger.debug(f'update event result: {event}')

        db.session.merge(event)
        db.session.commit()

        payload = {
            "success": True,
            "event": event
        }

    return payload


@convert_kwargs_to_snake_case
def delete_event_resolver(*args, **kwargs):

    event = Event.query.filter_by(id=kwargs['id']).first()
    logger.debug(f'delete event: {event}')

    if not event:
        payload = {
            "success": False,
            "errors": [f"Not found event with id: {kwargs['id']}"]
        }

    else:
        db.session.delete(event)
        db.session.commit()

        payload = {
            "success": True,
            "event": event
        }

    return payload
