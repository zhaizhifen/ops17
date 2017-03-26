"""empty message

Revision ID: 19c9ed5058f4
Revises: 505560cc374d
Create Date: 2017-03-26 21:19:43.654000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19c9ed5058f4'
down_revision = '505560cc374d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('department', sa.String(length=32), nullable=True),
    sa.Column('pm_id', sa.Integer(), nullable=True),
    sa.Column('dep_env', sa.String(length=32), nullable=True),
    sa.Column('sla', sa.String(length=32), nullable=True),
    sa.Column('check_point', sa.String(length=64), nullable=True),
    sa.Column('domain', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['pm_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_projects_department'), 'projects', ['department'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_projects_department'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###