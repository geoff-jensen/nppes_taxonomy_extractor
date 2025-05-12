import pandas as pd
from pathlib import Path

# --- Paths ---
INPUT_FILE = Path("../data/raw/npidata_pfile_20050523-20250511.csv")
OUTPUT_DIR = Path("../data/processed")
SAMPLE_DIR = Path("../data/samples")

# Ensure output folders exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

# --- Taxonomy Codes ---
INTERNAL_MED_CODE = "207R00000X"
GASTRO_CODE = "207RG0100X"

# --- Storage ---
internal_rows = []
gastro_rows = []

# --- Chunked Processing ---
chunksize = 100_000
print(f"Processing in chunks of {chunksize} rows...")

for chunk in pd.read_csv(INPUT_FILE, dtype=str, chunksize=chunksize, low_memory=False):

    # --- Internal Medicine Logic ---
    internal_matches = []
    for i in range(1, 16):
        code_col = f"Healthcare Provider Taxonomy Code_{i}"
        switch_col = f"Healthcare Provider Primary Taxonomy Switch_{i}"

        if code_col in chunk.columns and switch_col in chunk.columns:
            match = (chunk[code_col] == INTERNAL_MED_CODE) & (chunk[switch_col] == "Y")
            internal_matches.append(match)

    internal_combined = internal_matches[0]
    for match in internal_matches[1:]:
        internal_combined |= match

    internal_rows.append(chunk[internal_combined])

    # --- Gastroenterology Logic ---
    gastro_matches = []
    for i in range(1, 15 + 1):
        code_col = f"Healthcare Provider Taxonomy Code_{i}"
        switch_col = f"Healthcare Provider Primary Taxonomy Switch_{i}"

        if code_col in chunk.columns and switch_col in chunk.columns:
            match = (chunk[code_col] == GASTRO_CODE) & (chunk[switch_col] == "Y")
            gastro_matches.append(match)

    gastro_combined = gastro_matches[0]
    for match in gastro_matches[1:]:
        gastro_combined |= match

    gastro_rows.append(chunk[gastro_combined])

# --- Combine and Save ---
df_internal = pd.concat(internal_rows)
df_gastro = pd.concat(gastro_rows)

df_internal.to_csv(OUTPUT_DIR / "internal_medicine.csv", index=False)
df_gastro.to_csv(OUTPUT_DIR / "gastroenterology.csv", index=False)

# --- Create 10-row Samples ---
df_internal.head(10).to_csv(SAMPLE_DIR / "internal_sample.csv", index=False)
df_gastro.head(10).to_csv(SAMPLE_DIR / "gastro_sample.csv", index=False)

print("Done. Files saved to 'data/processed/' and 'data/samples/'.")
