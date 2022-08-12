"""init

Revision ID: 7df76e13d094
Revises: 
Create Date: 2022-08-11 17:17:30.493321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7df76e13d094'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # 테이블 생성
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False)
    )


def downgrade():
    # 테이블 삭제
    op.drop_table('jobs')
