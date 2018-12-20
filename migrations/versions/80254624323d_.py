"""empty message

Revision ID: 80254624323d
Revises: 0e3b22cf19a7
Create Date: 2018-12-19 09:16:29.522148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80254624323d'
down_revision = '0e3b22cf19a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'wfnj_userlog', 'wfnj_user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wfnj_userlog', type_='foreignkey')
    # ### end Alembic commands ###