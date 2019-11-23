"""empty message

Revision ID: a338c65d2302
Revises: 
Create Date: 2019-10-14 03:34:37.393663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a338c65d2302'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('apartments', sa.Column('baths', sa.Integer(), nullable=True))
    op.add_column('apartments', sa.Column('bedrooms', sa.Integer(), nullable=True))
    op.add_column('apartments', sa.Column('sleeps', sa.Integer(), nullable=True))
    op.add_column('apartments', sa.Column('sq_ft', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('apartments', 'sq_ft')
    op.drop_column('apartments', 'sleeps')
    op.drop_column('apartments', 'bedrooms')
    op.drop_column('apartments', 'baths')
    # ### end Alembic commands ###