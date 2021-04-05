"""empty message

Revision ID: 26a2d2ca6c0f
Revises: c0cf9729de9e
Create Date: 2021-04-05 16:49:47.713226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26a2d2ca6c0f'
down_revision = 'c0cf9729de9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=104), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
