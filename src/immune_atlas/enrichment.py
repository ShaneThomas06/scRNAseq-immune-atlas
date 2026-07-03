import pandas as pd


DEFAULT_EXCLUDED_PREFIXES = ("RPL", "RPS", "MT-")
DEFAULT_EXCLUDED_GENES = {"MALAT1", "NEAT1"}


def extract_upregulated_genes(
    de_table: pd.DataFrame,
    gene_col: str = "names",
    logfc_col: str = "logfoldchanges",
    min_logfc: float = 0.0,
) -> list[str]:
    """Extract genes with positive log-fold change from a differential expression table."""
    genes = (
        de_table[de_table[logfc_col] > min_logfc]
        .sort_values(logfc_col, ascending=False)[gene_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
    return genes


def filter_broad_genes(
    genes: list[str],
    excluded_prefixes: tuple[str, ...] = DEFAULT_EXCLUDED_PREFIXES,
    excluded_genes: set[str] = DEFAULT_EXCLUDED_GENES,
) -> list[str]:
    """Remove broad ribosomal, mitochondrial, and non-coding RNA signals."""
    return [
        gene for gene in genes
        if not gene.startswith(excluded_prefixes)
        and gene not in excluded_genes
    ]


def run_go_enrichment(
    genes: list[str],
    gene_sets: str = "GO_Biological_Process_2023",
    organism: str = "human",
    cutoff: float = 0.05,
) -> pd.DataFrame:
    """Run Enrichr Gene Ontology enrichment using gseapy."""
    import gseapy as gp

    enrichment = gp.enrichr(
        gene_list=genes,
        gene_sets=gene_sets,
        organism=organism,
        outdir=None,
        cutoff=cutoff,
    )

    return enrichment.results


def get_top_enrichment_terms(
    enrichment_results: pd.DataFrame,
    n_terms: int = 15,
    pvalue_col: str = "Adjusted P-value",
) -> pd.DataFrame:
    """Return top enriched terms ranked by adjusted p-value."""
    return enrichment_results.sort_values(pvalue_col).head(n_terms).copy()