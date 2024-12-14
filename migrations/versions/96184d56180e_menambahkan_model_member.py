"""menambahkan model member

Revision ID: 96184d56180e
Revises: 96df42c67f8a
Create Date: 2024-12-15 04:17:00.555823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96184d56180e'
down_revision = '96df42c67f8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nama_wilayah', sa.String(length=100), nullable=False),
    sa.Column('waktu_bergabung', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member')
    # ### end Alembic commands ###
