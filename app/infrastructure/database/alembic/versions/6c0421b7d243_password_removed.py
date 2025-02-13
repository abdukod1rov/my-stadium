"""password removed

Revision ID: 6c0421b7d243
Revises: 0748c9bd02a6
Create Date: 2024-05-16 15:37:32.095133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c0421b7d243'
down_revision: Union[str, None] = '0748c9bd02a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
