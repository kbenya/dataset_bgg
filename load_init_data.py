import pandas as pd

from sscutils import dump_dfs_to_trepos
from src.trepos import credits_table, details_table, micro_table, users_table, ratings_table

if __name__ == "__main__":
    droot = "data"
    
    credits_df = pd.read_json(f"{droot}/credits.json")
    details_df = pd.read_json(f"{droot}/details.json").T
    micro_df = pd.read_json(f"{droot}/micro.json").T
    users_df = pd.read_json(f"{droot}/users.json").T
    ratings_df = pd.read_json(f"{droot}/ratings.json")[["bg_id", "rating", "user_name", "timestamp"]]

    dump_dfs_to_trepos(None, [(credits_df, credits_table), (details_df, details_table), (micro_df, micro_table), (users_df, users_table), (ratings_df, ratings_table)])