"""creater user preferences

Revision ID: 26b423c62465
Revises: b97487a3de61
Create Date: 2026-09-26 12:36:51.565264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26b423c62465'
down_revision: Union[str, Sequence[str], None] = 'b97487a3de61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_preferences",
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column(
            "time_zone",
            sa.String(length=64),
            nullable=False,
            server_default=sa.text("'UTC'"),
        ),
        sa.Column("sleep_start", sa.Time(), nullable=True),
        sa.Column("sleep_end", sa.Time(), nullable=True),
        sa.Column(
            "reduced_motion",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.ForeignKeyConstraint(["user_id"], ["auth.users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_foreign_key(
        "user_preferences_user_id_fkey",
        "user_preferences",
        "users",
        ["user_id"],
        ["id"],
        source_schema="public",
        referent_schema="auth",
        ondelete="CASCADE",
    )

def downgrade() -> None:
    op.drop_constraint(
        "user_preferences_user_id_fkey",
        "user_preferences",
        schema="public",
        type_="foreignkey",
    )
    op.drop_table("user_preferences")
