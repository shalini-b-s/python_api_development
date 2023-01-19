"""create post table

Revision ID: 2969d0aeaecb
Revises: 
Create Date: 2023-01-19 09:56:31.401077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2969d0aeaecb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable = False, primary_key = True), 
    sa.Column('title', sa.String(), nullable = False))

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
