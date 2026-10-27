"""Byte Me: transparent, synthetic-data demonstration pipeline.

This script is an educational screening demo, not a validated biological predictor.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = {"Gene_ID", "Control", "Drought", "Salt"}

def load_expression(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if df.empty:
        raise ValueError("Input dataset is empty.")
    for col in ("Control", "Drought", "Salt"):
        df[col] = pd.to_numeric(df[col], errors="raise")
        if (df[col] < 0).any():
            raise ValueError(f"{col} values must be non-negative.")
    if (df["Control"] == 0).any():
        raise ValueError("Control values must be greater than zero to calculate fold change.")
    if df["Gene_ID"].duplicated().any():
        raise ValueError("Gene_ID values must be unique.")
    return df

def screen_candidates(df: pd.DataFrame, threshold: float = 1.5) -> pd.DataFrame:
    """Rank synthetic candidates by drought/control fold change.

    salt_ratio is shown as context; it is not a validated biological trade-off model.
    """
    out = df.copy()
    out["Drought_Fold_Change"] = out["Drought"] / out["Control"]
    out["Salt_Fold_Change"] = out["Salt"] / out["Control"]
    out["Drought_Response_Pct"] = (out["Drought_Fold_Change"] - 1.0) * 100
    out["Screening_Flag"] = out["Drought_Fold_Change"] >= threshold
    # Simple, explicit ranking heuristic for demonstration only.
    out["Demo_Rank_Score"] = (
        out["Drought_Fold_Change"] -
        0.25 * (1.0 - out["Salt_Fold_Change"]).clip(lower=0)
    )
    return out.sort_values("Demo_Rank_Score", ascending=False).reset_index(drop=True)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="data/rice_expression_demo.csv")
    parser.add_argument("--threshold", type=float, default=1.5)
    args = parser.parse_args()
    df = load_expression(args.data)
    ranked = screen_candidates(df, args.threshold)
    cols = ["Gene_ID", "Drought_Fold_Change", "Salt_Fold_Change",
            "Drought_Response_Pct", "Screening_Flag", "Demo_Rank_Score"]
    print("SYNTHETIC DATA — DEMONSTRATION OUTPUT ONLY")
    print(ranked[cols].to_string(index=False, formatters={
        "Drought_Fold_Change": "{:.2f}".format,
        "Salt_Fold_Change": "{:.2f}".format,
        "Drought_Response_Pct": "{:.1f}%".format,
        "Demo_Rank_Score": "{:.2f}".format,
    }))
    print("\nThese rankings are not validated gene-edit recommendations.")

if __name__ == "__main__":
    main()
