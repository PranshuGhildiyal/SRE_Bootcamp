"""add columns to students table.

Revision ID: 2ac85cc7c202
Revises: 9348051cf3d3
Create Date: 2024-12-06 03:59:25.733705

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2ac85cc7c202"
down_revision: Union[str, None] = "9348051cf3d3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("students", sa.Column("age", sa.Integer(), nullable=False))
    op.add_column(
        "students",
        sa.Column(
            "joining_date",
            sa.Date(),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("students", "age")
    op.drop_column("students", "joining_date")
    pass
