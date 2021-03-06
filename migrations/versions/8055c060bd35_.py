"""empty message

Revision ID: 8055c060bd35
Revises: 1de4b79c7fcc
Create Date: 2018-12-18 17:56:38.854422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8055c060bd35'
down_revision = '1de4b79c7fcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wfnj_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('pic_path', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_id')
    )
    op.add_column('wfnj_user', sa.Column('password', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'wfnj_userlog', 'wfnj_user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wfnj_userlog', type_='foreignkey')
    op.drop_column('wfnj_user', 'password')
    op.drop_table('wfnj_product')
    # ### end Alembic commands ###
