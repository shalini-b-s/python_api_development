"""add content column to post table

Revision ID: b73c3c1f94ab
Revises: 2969d0aeaecb
Create Date: 2023-01-19 12:04:02.526608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73c3c1f94ab'
down_revision = '2969d0aeaecb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
