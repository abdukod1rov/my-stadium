"""image-added

Revision ID: bc81a02f9d6a
Revises: e319e9c0e5ae
Create Date: 2024-05-12 14:46:43.873035

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc81a02f9d6a'
down_revision: Union[str, None] = 'e319e9c0e5ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    op.add_column('stadiums', sa.Column('image', sa.String(length=255), nullable=False))
    op.alter_column('stadiums', 'time_end',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stadiums', 'time_end',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.drop_column('stadiums', 'image')
    op.create_table('employee',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='employee_pkey')
    )
    # ### end Alembic commands ###
