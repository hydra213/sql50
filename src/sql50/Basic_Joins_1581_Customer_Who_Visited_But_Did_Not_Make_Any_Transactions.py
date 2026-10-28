import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = (
        pd.merge(visits, transactions, on="visit_id", how="left")
        .query("transaction_id.isna()")
        .fillna({"transaction_id": 1})
    )

    return (
        merged_df.groupby("customer_id", as_index=False)["transaction_id"]
        .count()
        .rename(columns={"transaction_id": "count_no_trans"})
    )
