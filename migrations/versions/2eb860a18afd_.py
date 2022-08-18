"""empty message

Revision ID: 2eb860a18afd
Revises: db2f3f8fd478
Create Date: 2022-08-17 11:57:43.826080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eb860a18afd'
down_revision = 'db2f3f8fd478'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # op.drop_constraint('address', 'contact')


def downgrade():
    pass
