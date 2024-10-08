"""'Init'

Revision ID: 17c303ff2079
Revises: 
Create Date: 2023-11-06 19:18:29.129530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '17c303ff2079'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('second_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.Column('favorite', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_id'), 'contacts', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_contacts_id'), table_name='contacts')
    op.drop_table('contacts')