"""add univ table

Revision ID: 9e58451eef81
Revises: ebdc961a3dd2
Create Date: 2020-10-17 06:40:46.633643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e58451eef81'
down_revision = 'ebdc961a3dd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('univ_info', sa.Column('logoPossible', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('univ_info', 'logoPossible')
    # ### end Alembic commands ###
