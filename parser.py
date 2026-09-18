from Bio import SeqIO
import pandas as pd
import io

def process_genomics_file(uploaded_file):
    #to determine format based on extension
    filename = uploaded_file.name.lower()
    file_format = "fastq" if filename.endswith((".fastq", "fq")) else "fasta"

    #read the uploaded file buffer as text/
    #get the uploaded file contents, convert bytes to text,
    #and create a file-like object in memory
    content = io.StringIO(uploaded_file.getvalue().decode("utf-8")) 

    parsed_records = []

    for record in SeqIO.parse(content, file_format):
        seq_str = str(record.seq).upper()
        seq_len = len(seq_str)

        #calculate G C contents -> percentage of G and C characters
        gc_count = seq_str.count("G") + seq_str.count("C")
        gc_pct = (gc_count / seq_len *100) if seq_len > 0 else 0

        record_info = {
            "sequence ID": record.id,
            "length (bp)": seq_len,
            "GC content (%)": round(gc_pct, 2) 
        }

        # FASTQ files include quality score per baes character 
        if file_format == "fastq" or file_format == "fq":
            quality_score = record.letter_annotations.get("phred_quality", [])
            avg_qual = sum(quality_score) / len(quality_score) if quality_score > 0 else 0
            record_info["Average Quality Score"] = round(avg_qual, 2)

        parsed_records.append(record_info)

    return pd.DataFrame(parsed_records), file_format


