"""third

Revision ID: 4d0fe4a8415b
Revises: a2b318c2a746
Create Date: 2024-04-08 17:17:21.391053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d0fe4a8415b'
down_revision: Union[str, None] = 'a2b318c2a746'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('user_id', sa.BigInteger(), nullable=False))
    op.create_foreign_key(None, 'todo', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'user_id')
    # ### end Alembic commands ###