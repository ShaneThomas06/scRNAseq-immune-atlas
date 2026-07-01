# scRNAseq Immune Atlas

Single-cell RNA-seq analysis of immune and epithelial remodeling in inflammatory bowel disease using Python and Scanpy.

## Project Goal

This project analyzes public single-cell RNA-seq data from inflammatory bowel disease tissue to explore how immune and epithelial cell populations differ between healthy and diseased intestinal samples.

The initial focus is ulcerative colitis colon tissue, with an emphasis on identifying disease-associated cell states, marker genes, and inflammatory transcriptional programs.

## Biological Questions

- Which cell types are present in healthy and IBD colon tissue?
- How do immune and epithelial cell populations differ between healthy and diseased samples?
- Which marker genes define major immune, epithelial, and stromal cell populations?
- Which genes are associated with inflammatory disease states?
- Can single-cell transcriptomic patterns reveal biologically meaningful differences between healthy and inflamed intestinal tissue?

## Planned Analysis

- Load and inspect public single-cell RNA-seq data
- Explore metadata including disease status, tissue region, donor/sample information, and cell type labels
- Perform quality control and preprocessing
- Normalize and transform gene expression counts
- Run PCA, neighborhood graph construction, clustering, and UMAP visualization
- Identify marker genes for major cell populations
- Compare healthy and diseased intestinal samples
- Visualize disease-associated immune and epithelial cell states
- Build an interactive Streamlit dashboard for exploring genes, cell types, and disease conditions

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