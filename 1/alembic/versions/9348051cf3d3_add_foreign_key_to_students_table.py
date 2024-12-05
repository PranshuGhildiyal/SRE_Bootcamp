"""add foreign key to students table.

Revision ID: 9348051cf3d3
Revises: 6cc88e48e075
Create Date: 2024-12-06 03:53:12.372024

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9348051cf3d3"
down_revision: Union[str, None] = "6cc88e48e075"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("students", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "students_users_fkey",
        source_table="students",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("students_users_fkey", table_name="students")
    op.drop_column("students", "owner_id")
    pass
