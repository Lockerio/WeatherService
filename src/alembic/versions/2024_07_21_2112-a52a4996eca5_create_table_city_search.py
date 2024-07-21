"""Create table city search

Revision ID: a52a4996eca5
Revises: 
Create Date: 2024-07-21 21:12:17.852524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a52a4996eca5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the CitySearches table
    op.create_table(
        'CitySearches',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('city_name', sa.String(), nullable=False),
        sa.Column('search_amount', sa.Integer(), nullable=False, default=1),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('city_name')
    )


def downgrade():
    # Drop the CitySearches table
    op.drop_table('CitySearches')
