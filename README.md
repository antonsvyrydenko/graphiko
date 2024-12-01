# Basic API project showing GraphQL + Flask usage

## Info

Test project which stores information about workers events and lets to perform CRUD on them. 

Tested with:
- `Python 3.10`
- `Flask 2.2.2`
- `Ubuntu 18.04`
- `Graphql-core 3.2.5`
- `Ariadne 0.23.0`
- `PostgreSQL 10.23`
- `Apollo Studio WEB Sandbox`

See `requirements.txt` to find out more libs used.

## Installation and Usage

- create DB
```
sudo -u postgres psql

create database gq;
create user gq with encrypted password 'gq';
grant all privileges on database gq to gq;
```

- install virtual environment
```
virtualenv -p python3.10 venv
```
- active environment
```
. venv/bin/activate
```
- install required libs
```
pip install -r requirements.txt
```
- init db
```
deactivate
./run.db migrate
./run.db upgrade
```
- start API
```
./run.sh api
```
- test API is running
```
curl -X GET http://127.0.0.1:55555/api/1.0/ping
```

You're done, API is ready to accept requests.

For sending requests you can use `Apollo Studio` or preferred `GraphQL` client.

## GraphQL queries examples

- get all user events
```
query GetUserEvents {
  getUserEvents(username: "Vasyl Ivanenko") {
    errors
    success
    event {
      id
      event_type
      title
      started_on
      finished_on
    }
  }
}
```
- get user events for `November 2024`
```
query GetUserMonthlyEvents {
  getUserMonthlyEvents(username: "Vasyl Ivanenko", date: "2024-11") {
    errors
    success
    event {
      id
      title
      event_type
      started_on
      finished_on
      description
    }
  }
}
```

- add new user event
```
mutation CreateEvent{
  createEvent(event_type: "Task", title: "MyApp - fix auth template",
    started_on: "2024-11-11 12:00:00", finished_on: "2024-11-11 14:00:00",
    username: "Vasyl Ivanenko") {
    errors
    success
    event {
      id
      event_type
      title
      started_on
      finished_on
      username
      description
      url
    }
  }
}
```

- update user event
```
mutation UpdateEvent {
  updateEvent(id: "135", finished_on: "2024-11-11 13:00:00") {
    errors
    success
    event {
      id
      title
      started_on
      finished_on
      username
    }
  }
}
```
- delete user event
```
mutation DeleteEvent {
  deleteEvent(id: "34") {
    success
    errors
    event {
      id
      event_type
      title
      username
    }
  }
}
```