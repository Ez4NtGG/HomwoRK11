"""empty message

Revision ID: 630f719091ab
Revises: 17c303ff2079
Create Date: 2023-11-07 01:41:20.720696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '630f719091ab'
down_revision: Union[str, None] = '17c303ff2079'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('contacts', sa.Column('last_name', sa.String(), nullable=True))
    op.drop_column('contacts', 'second_name')


def downgrade() -> None:
    op.add_column('contacts', sa.Column('second_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('contacts', 'last_name')