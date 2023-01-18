"""First

Revision ID: 4d6ab48b54ed
Revises: 
Create Date: 2023-01-16 22:58:24.194098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d6ab48b54ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'microblog',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('title', sa.String),
        sa.Column('text', sa.Text(350)),
        sa.Column('date', sa.Date)
    )


def downgrade() -> None:
    pass
