#!/usr/bin/env python3
"""
Safe migration runner for production.
Checks database connection and handles errors.
"""
import os
import time
import sys
import logging
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def wait_for_database(url, max_retries=30, delay=2):
    """Wait for database to be ready."""
    logger.info(f"Waiting for database connection...")
    
    for attempt in range(max_retries):
        try:
            engine = create_engine(url, connect_args={'connect_timeout': 5})
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            logger.info("✅ Database connection established!")
            return True
        except OperationalError as e:
            if attempt < max_retries - 1:
                logger.warning(f"Attempt {attempt + 1}/{max_retries}: Database not ready, retrying in {delay}s...")
                time.sleep(delay)
            else:
                logger.error(f"❌ Could not connect to database after {max_retries} attempts")
                logger.error(f"Error: {e}")
                return False
    
    return False

def run_migrations():
    """Run Alembic migrations."""
    # Get database URL from environment
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        logger.error("❌ DATABASE_URL environment variable not set!")
        sys.exit(1)
    
    # Wait for database
    if not wait_for_database(database_url):
        sys.exit(1)
    
    # Run migrations
    alembic_ini_path = os.path.join(os.path.dirname(__file__), 'alembic.ini')
    alembic_cfg = Config(alembic_ini_path)
    
    # Update the URL in config
    alembic_cfg.set_main_option('sqlalchemy.url', database_url)
    
    try:
        logger.info("Starting database migrations...")
        
        # Show current revision
        command.current(alembic_cfg, verbose=True)
        
        # Run migrations
        command.upgrade(alembic_cfg, "head")
        
        logger.info("✅ Database migrations completed successfully!")
        return True
    except Exception as e:
        logger.error(f"❌ Migration failed: {e}")
        return False

if __name__ == "__main__":
    success = run_migrations()
    sys.exit(0 if success else 1)
