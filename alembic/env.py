import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.database import DATABASE_URL
config = context.config
config.set_main_option('sqlalchemy.url', DATABASE_URL)

fileConfig(config.config_file_name, disable_existing_loggers=False)

from app.models.url import Base
target_metadata = Base.metadata

from app.models import url 

config.set_section_option('alembic', 'target_metadata', repr(target_metadata))

