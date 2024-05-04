"""relation

Revision ID: 6f930af76c8f
Revises: 090344216b2f
Create Date: 2024-04-18 18:53:18.705085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f930af76c8f'
down_revision: Union[str, None] = '090344216b2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_roles_user_id_fkey', 'user_roles', type_='foreignkey')
    op.drop_constraint('user_roles_role_id_fkey', 'user_roles', type_='foreignkey')
    op.create_foreign_key(None, 'user_roles', 'role', ['role_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'user_roles', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_roles', type_='foreignkey')
    op.drop_constraint(None, 'user_roles', type_='foreignkey')
    op.create_foreign_key('user_roles_role_id_fkey', 'user_roles', 'role', ['role_id'], ['id'])
    op.create_foreign_key('user_roles_user_id_fkey', 'user_roles', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###