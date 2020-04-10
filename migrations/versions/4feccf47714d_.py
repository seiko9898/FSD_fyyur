"""empty message

Revision ID: 4feccf47714d
Revises: 652c307fb26a
Create Date: 2020-04-10 07:28:48.484823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4feccf47714d'
down_revision = '652c307fb26a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
