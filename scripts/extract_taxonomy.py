import pandas as pd
from pathlib import Path

# Paths
INPUT_FILE = Path("../data/raw/npidata_pfile_20050523-2025011.csv")
OUTPUT_DIR = Path("../datra/processed")
SAMPLE_DIR = Path("../data/sample")


# Taxonomy Codes
INTERNAL_MED_CODE = "207R00000X"
GASTRO_CODE = "207RG0100X"


#Storage
internal_rows = []
gastro_rows = []

# Chunked Processing
chunksize = 100_000
print(f"Processing in chunks of {chunksize} rows...")

import pandas as pd
from pathlib import Path

# --- Paths ---
INPUT_FILE = Path("../data/raw/npidata_pfile_20050523-20250511.csv")
OUTPUT_DIR = Path("../data/processed")
SAMPLE_DIR = Path("../data/samples")

# Ensure output folders exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

# --- Filtering Criteria ---
INTERNAL_MED_CODE = "207R00000X"
GASTRO_CODE = "207RG0100X"
PRIMARY_SWITCH = "Y"

# --- Storage ---
internal_rows = []
gastro_rows = []

# --- Chunked Processing ---
chunksize = 100_000
print(f"Processing in chunks of {chunksize} rows...")

for chunk in pd.read_csv(INPUT_FILE, dtype=str, chunksize=chunksize, low_memory=False):
    internal = chunk[
        (chunk["Healthcare Provider Taxonomy Code_1"] == INTERNAL_MED_CODE) &
        (chunk["Healthcare Provider Primary Taxonomy Switch_1"] == PRIMARY_SWITCH)
    ]
    gastro = chunk[
        (chunk["Healthcare Provider Taxonomy Code_1"] == GASTRO_CODE) &
        (chunk["Healthcare Provider Primary Taxonomy Switch_1"] == PRIMARY_SWITCH)
    ]
    internal_rows.append(internal)
    gastro_rows.append(gastro)

# --- Combine + Save ---
df_internal = pd.concat(internal_rows)
df_gastro = pd.concat(gastro_rows)

internal_path = OUTPUT_DIR / "internal_medicine.csv"
gastro_path = OUTPUT_DIR / "gastroenterology.csv"

df_internal.to_csv(internal_path, index=False)
df_gastro.to_csv(gastro_path, index=False)

# --- Create 10-row samples ---
df_internal.head(10).to_csv(SAMPLE_DIR / "internal_sample.csv", index=False)
df_gastro.head(10).to_csv(SAMPLE_DIR / "gastro_sample.csv", index=False)

print(f"Done! Outputs saved to:\n{internal_path}\n{gastro_path}")
