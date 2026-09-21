import streamlit as st
import matplotlib.pyplot as plt
from parser import process_genomics_file

st.set_page_config(page_title="GENOMIC DATA REVIEWER", layout="wide")

st.title("Genomic Data File Analyzer")
st.write("Upload a file to extract sequence statistics.")

uploaded_file = st.sidebar.file_uploader(
    "Choose a file", type=["fasta", "fa", "fastq", "fq"]
)

if uploaded_file is not None:
    # 1. Parse file
    df, file_format = process_genomics_file(uploaded_file)

    # Check if file parsed properly
    if df.empty:
        st.error("No valid genomic sequences were found in this file. Please check the file contents!")
    else:
        # 2. Display overview cards
        st.success(f"Successfully loaded {file_format.upper()} file!")

        c1, c2, c3 = st.columns(3)
        c1.metric("Total Sequences", len(df))
        c2.metric("Average Length", f"{int(df['Length (bp)'].mean())} bp")
        c3.metric("Average GC Content", f"{round(df['GC Content (%)'].mean(), 1)}%")

        # 3. Display data table
        st.subheader("Sequence Details")
        st.dataframe(df, use_container_width=True)

        #add csv download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label = "📥 Download Summary CSV",
            data = csv,
            file_name = "genomic_summary.csv",
            mime = "tet/csv",
        )

        # 4. Render charts
        st.subheader("Data Distribution")
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

        # Chart 1: Length distribution
        axes[0].hist(df["Length (bp)"], color="steelblue", edgecolor="black", bins=15)
        axes[0].set_title("Sequence Length Histogram")
        axes[0].set_xlabel("Length (bp)")
        axes[0].set_ylabel("Count")

        # Chart 2: GC content distribution
        axes[1].hist(df["GC Content (%)"], color="#DD8452", edgecolor="black", bins=15)
        axes[1].set_title("GC Content Histogram")
        axes[1].set_xlabel("GC Content (%)")
        axes[1].set_ylabel("Count")

        st.pyplot(fig)

else:
    st.info("Upload your 'sample.fasta' or 'sample.fastq' using the sidebar to test.")