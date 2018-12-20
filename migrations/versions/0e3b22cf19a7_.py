"""empty message

Revision ID: 0e3b22cf19a7
Revises: 8055c060bd35
Create Date: 2018-12-18 17:57:40.810966

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0e3b22cf19a7'
down_revision = '8055c060bd35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('wfnj_user', 'tel',
               existing_type=mysql.VARCHAR(length=11),
               nullable=True)
    op.create_foreign_key(None, 'wfnj_userlog', 'wfnj_user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wfnj_userlog', type_='foreignkey')
    op.alter_column('wfnj_user', 'tel',
               existing_type=mysql.VARCHAR(length=11),
               nullable=False)
    # ### end Alembic commands ###
