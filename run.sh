#!/usr/bin/env bash

if [ "$1" = "" ]; then
    echo "Main usage:
    ./run.sh db [init | migrate | upgrade] - perform db actions
    ./run.sh api - launch service API
    "
else
    case "$1" in
        freeze)
            source venv/bin/activate
            pip freeze | grep -v "pkg-resources" > requirements.txt
        ;;
        db)
            source venv/bin/activate
            export FLASK_APP=manage.py
            flask db $2
        ;;
        *)
            source venv/bin/activate
            python ./manage.py $1
    esac
fi
