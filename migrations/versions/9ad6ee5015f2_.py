"""empty message

Revision ID: 9ad6ee5015f2
Revises: 
Create Date: 2024-11-30 15:17:47.829396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad6ee5015f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('event_type', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('started_on', sa.DateTime(), nullable=False),
    sa.Column('finished_on', sa.DateTime(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###
