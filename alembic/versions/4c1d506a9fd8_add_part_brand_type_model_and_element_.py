"""Add Part, Brand, Type, Model and Element tables

Revision ID: 4c1d506a9fd8
Revises: 945c0c4fb9da
Create Date: 2023-01-07 00:10:23.174510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c1d506a9fd8'
down_revision = '945c0c4fb9da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('part',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('part_number', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand_name', sa.String(length=30), nullable=True),
    sa.Column('part_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['part_id'], ['part.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('element',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('element_name', sa.String(), nullable=True),
    sa.Column('part_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['part_id'], ['part.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(), nullable=True),
    sa.Column('part_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['part_id'], ['part.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(), nullable=True),
    sa.Column('part_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['part_id'], ['part.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('type')
    op.drop_table('model')
    op.drop_table('element')
    op.drop_table('brand')
    op.drop_table('part')
    # ### end Alembic commands ###
