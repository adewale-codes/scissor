"""create_urls_table

Revision ID: a896c997284e
Revises: 088b25135452
Create Date: 2024-02-20 12:27:14.735606

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a896c997284e'
down_revision = '088b25135452'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'urls',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('original_url', sa.String(), nullable=True),
        sa.Column('short_url', sa.String(), nullable=True),
        sa.Column('custom_alias', sa.String(), nullable=True),
        sa.Column('click_count', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('urls')
