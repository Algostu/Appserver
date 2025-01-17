"""add univ table

Revision ID: 6e33cce4a7ad
Revises: d77a26a6b1c8
Create Date: 2020-10-17 06:11:31.538440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e33cce4a7ad'
down_revision = 'd77a26a6b1c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('univ_info',
    sa.Column('univID', sa.Integer(), nullable=False),
    sa.Column('univName', sa.String(length=100, collation='utf8_unicode_ci'), nullable=True),
    sa.Column('subRegion', sa.String(length=100, collation='utf8_unicode_ci'), nullable=True),
    sa.Column('homePage', sa.String(length=1000, collation='utf8_unicode_ci'), nullable=True),
    sa.PrimaryKeyConstraint('univID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('univ_info')
    # ### end Alembic commands ###
