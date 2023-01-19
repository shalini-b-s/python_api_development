"""add foreign key to post table

Revision ID: 4564d7dc89c0
Revises: d249905f9790
Create Date: 2023-01-19 12:27:48.410301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4564d7dc89c0'
down_revision = 'd249905f9790'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table= 'posts', referent_table= 'users', local_cols = ['owner_id'], remote_cols= ['id'], ondelete= 'CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
