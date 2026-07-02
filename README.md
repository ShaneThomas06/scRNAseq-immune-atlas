# scRNAseq Immune Atlas

Single-cell RNA-seq analysis of immune and epithelial remodeling in inflammatory bowel disease using Python and Scanpy.

## Project Goal

This project analyzes public single-cell RNA-seq data from inflammatory bowel disease tissue to explore how immune cell populations and transcriptional states differ between healthy, non-inflamed, and inflamed intestinal samples.

The current analysis focuses on immune cells from ulcerative colitis colon tissue, with downstream emphasis on disease-associated macrophage inflammatory programs.

## Biological Questions

- Which immune cell populations are present in healthy and IBD-associated intestinal tissue?
- How does immune cell composition differ across healthy, non-inflamed, and inflamed tissue?
- Do annotated immune clusters express expected canonical marker genes?
- Which macrophage genes are associated with inflamed intestinal tissue?
- Can single-cell transcriptomic patterns reveal biologically meaningful inflammatory programs in IBD?

## Completed Analysis

### 1. Data Exploration

The first notebook loads immune-cell single-cell RNA-seq data, aligns expression data with metadata, and summarizes immune cell composition across tissue conditions.

Outputs include:

- Immune cell composition table by condition
- Composition change table comparing healthy and inflamed tissue
- Heatmap of major immune cell populations across healthy, non-inflamed, and inflamed samples

### 2. Marker Gene Analysis

The second notebook identifies marker genes for annotated immune clusters and validates major immune identities using canonical marker genes.

Key findings:

- T cell clusters express `CD3D`, `CD3E`, and `TRAC`
- Regulatory T cells show markers including `FOXP3`, `IL2RA`, and `CTLA4`
- B/plasma cell populations show `MS4A1`, `CD79A`, `MZB1`, and `JCHAIN`
- Myeloid populations show `LYZ`, `S100A8`, and `S100A9`
- Mast cell clusters show `TPSAB1` and `KIT`

### 3. Disease-Associated Expression Analysis

The third notebook compares macrophage gene expression between inflamed and healthy tissue.

Initial findings suggest that inflamed macrophages show stronger expression of inflammatory myeloid genes including:

- `S100A8`
- `S100A9`
- `S100A6`
- `LYZ`

These genes support the presence of disease-associated inflammatory macrophage states in IBD tissue.

## Repository Structure

```text
app/                 Streamlit dashboard prototype
data/                Raw and processed data, not tracked in Git
notebooks/           Analysis notebooks
results/figures/     Saved figures
results/tables/      Saved result tables
src/immune_atlas/    Reusable project code