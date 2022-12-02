"""empty message

Revision ID: b9a5e3691988
Revises: edb31dc45747
Create Date: 2022-11-29 14:06:24.029360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a5e3691988'
down_revision = 'edb31dc45747'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('number', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_number_number')
        batch_op.create_index(batch_op.f('ix_number_value'), ['value'], unique=False)
        batch_op.drop_column('number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('number', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number', sa.INTEGER(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_number_value'))
        batch_op.create_index('ix_number_number', ['number'], unique=False)
        batch_op.drop_column('value')

    # ### end Alembic commands ###
