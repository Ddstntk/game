"""empty message

Revision ID: e68194b6391a
Revises: 7b6c8994ab9b
Create Date: 2019-02-21 02:30:24.365769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e68194b6391a'
down_revision = '7b6c8994ab9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('agility', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('stamina', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('strength', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'strength')
    op.drop_column('user', 'stamina')
    op.drop_column('user', 'agility')
    # ### end Alembic commands ###
