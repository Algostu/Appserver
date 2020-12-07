"""empty message

Revision ID: d1d94c969d5e
Revises: 377841972a48
Create Date: 2020-12-05 20:19:41.533046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1d94c969d5e'
down_revision = '377841972a48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('univ_info', sa.Column('admission', sa.String(length=500, collation='utf8_unicode_ci'), nullable=True))
    op.add_column('univ_info', sa.Column('engname', sa.String(length=150, collation='utf8_unicode_ci'), nullable=True))
    op.add_column('univ_info', sa.Column('youtubue', sa.String(length=500, collation='utf8_unicode_ci'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('univ_info', 'youtubue')
    op.drop_column('univ_info', 'engname')
    op.drop_column('univ_info', 'admission')
    # ### end Alembic commands ###
