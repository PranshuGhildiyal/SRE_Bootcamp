"""create students table

Revision ID: f203350b016e
Revises: 
Create Date: 2024-12-06 03:17:37.269766

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f203350b016e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students",
        sa.Column(
            "id", sa.Integer(), autoincrement=True, primary_key=True, nullable=False
        ),
        sa.Column("name", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("students")
    pass
