import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered_df = views[(views["viewer_id"] == views["author_id"])][
        ["author_id"]
    ].drop_duplicates()

    return filtered_df.rename(columns={"author_id": "id"}).sort_values(
        by="id", ascending=True
    )
