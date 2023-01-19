"""add user table

Revision ID: d249905f9790
Revises: b73c3c1f94ab
Create Date: 2023-01-19 12:11:08.053913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd249905f9790'
down_revision = 'b73c3c1f94ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
    sa.Column('id', sa.Integer(), nullable = False),
    sa.Column('email', sa.String(), nullable = False), 
    sa.Column('password', sa.String(), nullable = False), 
    sa.Column('created_at', sa.TIMESTAMP(timezone = True), 
    server_default = sa.text('now()'), nullable = False), 
    sa.PrimaryKeyConstraint('id'), 
    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
