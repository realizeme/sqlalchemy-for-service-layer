"""Update relationship

Revision ID: ccd916e3e182
Revises: 2a7c683e1724
Create Date: 2021-05-11 01:46:30.428057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd916e3e182'
down_revision = '2a7c683e1724'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('image_dataset_id_fkey', 'image', type_='foreignkey')
    op.create_foreign_key(None, 'image', 'dataset', ['dataset_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.create_foreign_key('image_dataset_id_fkey', 'image', 'dataset', ['dataset_id'], ['id'])
    # ### end Alembic commands ###