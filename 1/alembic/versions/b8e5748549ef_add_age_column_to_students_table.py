"""add age column to students table

Revision ID: b8e5748549ef
Revises: f203350b016e
Create Date: 2024-12-06 03:39:47.337240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8e5748549ef'
down_revision: Union[str, None] = 'f203350b016e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
