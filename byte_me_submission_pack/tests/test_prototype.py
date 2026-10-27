import sys
from pathlib import Path
import unittest
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prototype import load_expression, screen_candidates

DATA = Path(__file__).resolve().parents[1] / "data" / "rice_expression_demo.csv"

class PrototypeTests(unittest.TestCase):
    def test_sample_data_loads(self):
        df = load_expression(DATA)
        self.assertEqual(len(df), 5)

    def test_screening_flags_high_drought_response(self):
        ranked = screen_candidates(load_expression(DATA), threshold=1.5)
        row = ranked.loc[ranked["Gene_ID"] == "Os01g0100100"].iloc[0]
        self.assertTrue(bool(row["Screening_Flag"]))

    def test_missing_column_rejected(self):
        bad = pd.DataFrame({"Gene_ID": ["g1"], "Control": [1], "Drought": [2]})
        with self.assertRaises(ValueError):
            screen_candidates(load_expression_from_frame(bad))

def load_expression_from_frame(df):
    missing = {"Gene_ID", "Control", "Drought", "Salt"} - set(df.columns)
    if missing:
        raise ValueError("Missing required columns")
    return df

if __name__ == "__main__":
    unittest.main()
