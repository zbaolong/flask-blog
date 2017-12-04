"""..

Revision ID: 6c46bad534f8
Revises: e7e9c98aad8d
Create Date: 2017-12-04 20:06:42.500127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c46bad534f8'
down_revision = 'e7e9c98aad8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('post_author_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_comment_post_author_id'), 'comment', ['post_author_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_post_author_id'), table_name='comment')
    op.drop_column('comment', 'post_author_id')
    # ### end Alembic commands ###
