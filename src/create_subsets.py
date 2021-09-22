from sscutils import dump_dfs_to_trepos

from .trepos import credits_table, details_table, micro_table, users_table, ratings_table

def create_subsets(subset_name, num_bg_ratings = 10):
    """create subsets that are described in the config of the repo"""
    credits_df = credits_table.get_full_df()
    details_df = details_table.get_full_df()
    micro_df = micro_table.get_full_df()
    users_df = users_table.get_full_df()
    ratings_df = ratings_table.get_full_df().iloc[:num_bg_ratings, :]

    dump_dfs_to_trepos(subset_name, [(credits_df, credits_table), (details_df, details_table), (micro_df, micro_table), (users_df, users_table), (ratings_df, ratings_table)])
