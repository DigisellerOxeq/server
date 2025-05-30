"""change lot type2

Revision ID: fd3348e7159e
Revises: d4afd7a43e88
Create Date: 2025-05-26 22:29:33.533351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd3348e7159e'
down_revision: Union[str, None] = 'c726278698e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE lottype ADD VALUE IF NOT EXISTS 'telegram'")
    op.execute("ALTER TYPE lottype ADD VALUE IF NOT EXISTS 'steam'")
    op.execute("ALTER TYPE lottype ADD VALUE IF NOT EXISTS 'itunes'")


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
