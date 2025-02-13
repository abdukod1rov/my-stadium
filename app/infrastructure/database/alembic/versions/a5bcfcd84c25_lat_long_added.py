"""lat long added

Revision ID: a5bcfcd84c25
Revises: 6c0421b7d243
Create Date: 2024-05-30 15:19:49.089728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5bcfcd84c25'
down_revision: Union[str, None] = '6c0421b7d243'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stadiums', sa.Column('lat', sa.String(length=100), nullable=True))
    op.add_column('stadiums', sa.Column('long', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stadiums', 'long')
    op.drop_column('stadiums', 'lat')
    # ### end Alembic commands ###
