# scRNAseq Immune Atlas

A single-cell RNA-seq analysis project exploring immune cell populations, marker genes, and disease-associated transcriptional states using Python and Scanpy.

## Project Goal

This project analyses public single-cell RNA-seq data to identify immune cell populations, visualize cellular heterogeneity, and compare gene expression patterns across biological conditions such as healthy and diseased tissue.

## Planned Analysis

- Load and inspect public single-cell RNA-seq data
- Perform quality control and preprocessing
- Normalise and transform gene expression counts
- Run PCA, neighborhood graph construction, clustering, and UMAP
- Identify marker genes for immune cell clusters
- Compare cell states between biological conditions
- Build an interactive Streamlit dashboard for exploration

## Tools

- Python
- Scanpy
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- Streamlit

## Repository Structure

```text
app/                 Streamlit dashboard
data/                Raw and processed data, not tracked in Git
notebooks/           Exploratory analysis notebooks
results/             Figures and output tables
src/immune_atlas/    Reusable project code