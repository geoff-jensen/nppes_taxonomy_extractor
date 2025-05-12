# 🩺 NPPES Taxonomy Extractor

A Python-based data extraction tool that filters the official NPPES dataset (~7M+ records) to identify providers with **Internal Medicine** and **Gastroenterology** as their **primary specialty**, using taxonomy codes.

This tool is designed to efficiently process multi-GB public datasets in memory-safe chunks and output both full result sets and lightweight samples for review or delivery.

---

## 📦 Features

- ✅ Processes massive CSVs (~6GB uncompressed) with `pandas` chunking
- ✅ Identifies **primary taxonomy** across all 15 possible taxonomy fields
- ✅ Filters for:
  - Internal Medicine (`207R00000X`)
  - Gastroenterology (`207RG0100X`)
- ✅ Outputs:
  - Full filtered CSVs *(optional)*
  - Sample files (10-row CSVs) for GitHub or client demo
- ✅ Clean project architecture ready for GitHub or freelance delivery
- ✅ Easily extensible to support other taxonomy codes

---

## 📁 Project Structure

```
nppes_taxonomy_extractor/
├── data/
│   ├── raw/          # Unzipped NPPES files
│   ├── processed/    # Filtered full output files (optional)
│   └── samples/      # 10-row preview files
├── scripts/
│   └── extract_taxonomy.py
├── .gitignore
├── requirements.txt
├── README.md
└── venv/
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Place Raw Data

Unzip `NPPES_Data_Dissemination_May_2025_V2.zip` and place the `npidata_pfile_*.csv` into:

```
data/raw/
```

### 3. Run the Script

```bash
cd scripts
python extract_taxonomy.py
```

The script will:
- Read the CSV in 100,000-row chunks
- Filter for providers with the specified primary taxonomy
- Output results to:
  - `data/processed/internal_medicine.csv` *(optional)*
  - `data/processed/gastroenterology.csv` *(optional)*
  - `data/samples/internal_sample.csv` (10-row preview)
  - `data/samples/gastro_sample.csv` (10-row preview)

---

## 🧠 Why This Project Matters

This tool demonstrates how to:

- Handle **large-scale public data** reliably
- Implement **multi-column conditional filtering**
- Build **clean, maintainable automation tools**
- Follow modern Python best practices with project structure and virtual environments

---

## 🏷️ Tags

`python` `pandas` `data cleaning` `csv processing` `public datasets` `taxonomy codes` `healthcare data` `automation` `freelance-ready` `portfolio project`

---

## 📌 Notes

- Future enhancements could include CLI argument support and dynamic taxonomy filtering for custom use cases.

---

## 👤 Author

Geoff Jensen  
*Freelance Python Developer | Data Automation | Cloud Learner*