"""create_urls_table

Revision ID: 4944bc2b817c
Revises: a896c997284e
Create Date: 2024-02-20 12:37:51.248406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4944bc2b817c'
down_revision: Union[str, None] = 'a896c997284e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'urls',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('original_url', sa.String(), nullable=True),
        sa.Column('short_url', sa.String(), nullable=True),
        sa.Column('custom_alias', sa.String(), nullable=True),
        sa.Column('click_count', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('urls')
