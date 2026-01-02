#!/bin/bash
# Database management script

case "$1" in
    "migrate")
        alembic revision --autogenerate -m "$2"
        ;;
    "upgrade")
        alembic upgrade head
        ;;
    "downgrade")
        alembic downgrade -1
        ;;
    "history")
        alembic history
        ;;
    "reset")
        echo "⚠️  WARNING: This will drop all tables!"
        read -p "Continue? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]
        then
            python -c "from app.database import engine, Base; Base.metadata.drop_all(bind=engine)"
            alembic upgrade head
        fi
        ;;
    *)
        echo "Usage: $0 {migrate|upgrade|downgrade|history|reset}"
        exit 1
        ;;
esac
