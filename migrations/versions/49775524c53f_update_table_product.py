"""update table product

Revision ID: 49775524c53f
Revises: fa56f359ebe8
Create Date: 2024-11-22 02:43:48.060297

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '49775524c53f'
down_revision = 'fa56f359ebe8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_file', sa.Text(), nullable=True))
        batch_op.drop_column('img_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_url', mysql.TEXT(), nullable=True))
        batch_op.drop_column('img_file')

    # ### end Alembic commands ###
