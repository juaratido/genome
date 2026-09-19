from Bio import SeqIO
import pandas as pd
import io

def process_genomics_file(uploaded_file):
    # Determine format based on extension
    filename = uploaded_file.name.lower()
    file_format = "fastq" if filename.endswith((".fastq", ".fq")) else "fasta"

    # Read uploaded file buffer into string stream
    content = io.StringIO(uploaded_file.getvalue().decode("utf-8"))

    parsed_records = []

    for record in SeqIO.parse(content, file_format):
        seq_str = str(record.seq).upper()
        seq_len = len(seq_str)

        # Calculate GC Content
        gc_count = seq_str.count("G") + seq_str.count("C")
        gc_pct = (gc_count / seq_len * 100) if seq_len > 0 else 0

        record_info = {
            "Sequence ID": record.id,
            "Length (bp)": seq_len,
            "GC Content (%)": round(gc_pct, 2)
        }

        # FASTQ Quality Score Processing
        if file_format == "fastq":
            quality_score = record.letter_annotations.get("phred_quality", [])
            # FIX: Check the length of the list, not the list itself against > 0
            avg_qual = sum(quality_score) / len(quality_score) if len(quality_score) > 0 else 0
            record_info["Avg Quality Score"] = round(avg_qual, 2)

        parsed_records.append(record_info)

    return pd.DataFrame(parsed_records), file_format