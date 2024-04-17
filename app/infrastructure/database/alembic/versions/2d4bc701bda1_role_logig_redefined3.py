"""role-logig-redefined3

Revision ID: 2d4bc701bda1
Revises: 2a5d7cf3c933
Create Date: 2024-04-16 13:21:24.218109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d4bc701bda1'
down_revision: Union[str, None] = '2a5d7cf3c933'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_roles', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_roles', 'role_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_roles', 'role_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_roles', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###