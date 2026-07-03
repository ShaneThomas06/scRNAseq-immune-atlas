# Methods

## Dataset

This project analyzes a public single-cell RNA-seq dataset from inflammatory bowel disease intestinal tissue. The current analysis focuses on the immune-cell compartment.

The immune-cell data are stored as separate raw files:

- `Imm.barcodes2.tsv`: immune cell barcodes
- `Imm.genes.tsv`: gene names
- `gene_sorted-Imm.matrix.mtx`: sparse gene expression matrix
- `Imm.tsne.txt`: published t-SNE coordinates
- `all.meta2.txt`: cell-level metadata

Raw and processed data files are not tracked in Git because of file size.

## Data Loading

The raw immune-cell expression matrix is loaded from Matrix Market format and combined with immune cell barcodes and gene names. Because the raw matrix is stored as genes by cells, it is transposed before creating a Scanpy `AnnData` object.

Cell-level metadata are matched to immune cell barcodes and stored in `adata.obs`.

## Data Object

The main analysis object is a Scanpy `AnnData` object.

- `adata.X`: gene expression matrix
- `adata.obs`: cell metadata
- `adata.var_names`: gene names
- `adata.obs_names`: cell barcodes

The processed object is saved locally as:

```text
data/processed/immune_cells_with_metadata.h5ad