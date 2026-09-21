# 🧬 Genomic Data File Analyzer

A fast, interactive web-based genomics utility built with **Python**, **Streamlit**, and **Biopython**. This application parses sequence files (FASTA and FASTQ formats) to perform automated quality control checks, metrics calculation, and distribution visualizations.

---

## ✨ Features

- **Multi-Format Support**: Reads and parses `.fasta`, `.fa`, `.fastq`, and `.fq` file formats seamlessly.
- **Key Metrics Calculation**:
  - Total sequence count
  - Mean sequence length (bp)
  - Average GC Content (%)
  - Mean Phred Quality Score (_FASTQ only_)
- **Interactive Data Inspection**: Displays parsed record metrics in an interactive, searchable tabular view.
- **Visual Analytics**: Automatically generates side-by-side distribution histograms for:
  1. Sequence Length Distribution
  2. GC Content (%) Distribution

---

## 🛠️ Tech Stack

- **Frontend / Framework**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Genomic Sequence Parsing**: [Biopython](https://biopython.org/)
- **Data Visualization**: [Matplotlib](https://matplotlib.org/)

---

## 📁 Repository Structure

```text
genome/
├── app.py              # Main Streamlit application interface
├── parser.py           # Core logic for parsing FASTA/FASTQ files using Biopython
├── generate_data.py    # Utility script to generate test FASTA/FASTQ files
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```
