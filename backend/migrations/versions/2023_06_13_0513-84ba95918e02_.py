"""empty message

Revision ID: 84ba95918e02
Revises: a8a859bfb7b9
Create Date: 2023-06-13 05:13:53.970759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84ba95918e02'
down_revision = 'a8a859bfb7b9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('reaction_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('like')
    op.add_column('video', sa.Column('count_reactions', sa.Integer(), nullable=True))
    op.drop_column('video', 'count_dislikes')
    op.drop_column('video', 'count_likes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('count_likes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('video', sa.Column('count_dislikes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('video', 'count_reactions')
    op.create_table('like',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('video_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='like_user_id_fkey'),
    sa.ForeignKeyConstraint(['video_id'], ['video.id'], name='like_video_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='like_pkey')
    )
    op.drop_table('reaction')
    # ### end Alembic commands ###