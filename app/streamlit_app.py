from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = PROJECT_ROOT / "results" / "figures"
TABLES_DIR = PROJECT_ROOT / "results" / "tables"

st.set_page_config(
    page_title="scRNAseq Immune Atlas",
    layout="wide",
    initial_sidebar_state="expanded",
)


FIGURES = {
    "Immune composition": {
        "file": "top_immune_clusters_by_condition_heatmap.png",
        "caption": "Major immune cell populations across healthy, non-inflamed, and inflamed intestinal tissue.",
    },
    "Canonical marker validation": {
        "file": "canonical_marker_dotplot.png",
        "caption": "Canonical immune markers validate major cluster identities.",
    },
    "Macrophage inflammatory genes": {
        "file": "macrophage_inflammatory_gene_dotplot.png",
        "caption": "Selected inflammatory and myeloid genes across macrophage tissue conditions.",
    },
    "Macrophage pathway enrichment": {
        "file": "macrophage_go_enrichment_filtered.png",
        "caption": "GO biological processes enriched among genes upregulated in inflamed macrophages.",
    },
}

TABLES = {
    "Immune cluster composition by condition": "immune_cluster_composition_by_condition.csv",
    "Immune cluster composition changes": "immune_cluster_composition_changes.csv",
    "Selected cluster marker genes": "selected_cluster_marker_genes.csv",
    "Macrophage significant DE genes": "macrophage_inflamed_vs_healthy_significant_genes.csv",
    "Filtered macrophage GO enrichment": "macrophage_go_enrichment_filtered.csv",
}


st.markdown(
    """
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

.main-title {
    font-size: 2.6rem;
    font-weight: 750;
    margin-bottom: 0.2rem;
    color: #123C3D;
}

.subtitle {
    font-size: 1.05rem;
    color: #4B635F;
    margin-bottom: 1.5rem;
}

.section-header {
    font-size: 1.45rem;
    font-weight: 700;
    margin-top: 1rem;
    margin-bottom: 0.75rem;
    color: #123C3D;
}

.finding-card {
    border: 1px solid #C9D8D5;
    border-left: 5px solid #D9903D;
    border-radius: 8px;
    padding: 1rem 1.1rem;
    background: #FBFDFB;
    min-height: 150px;
    box-shadow: 0 1px 8px rgba(18, 60, 61, 0.06);
}

.finding-title {
    font-weight: 700;
    color: #123C3D;
    margin-bottom: 0.35rem;
}

.finding-body {
    color: #334A46;
    font-size: 0.95rem;
    line-height: 1.45;
}

.metric-card {
    border: 1px solid #C9D8D5;
    border-radius: 8px;
    padding: 0.85rem 1rem;
    background: #EEF6F4;
    color: #123C3D;
}

.small-note {
    color: #5F746F;
    font-size: 0.88rem;
}

hr {
    margin-top: 1.25rem;
    margin-bottom: 1.25rem;
}

[data-testid="stSidebar"] {
    background-color: #123C3D;
}

[data-testid="stSidebar"] * {
    color: #F7FAF9;
}

.stRadio > div {
    gap: 0.35rem;
}

div[data-testid="stMetric"] {
    background-color: #EEF6F4;
    border-radius: 8px;
}
</style>
""",
    unsafe_allow_html=True,
)

@st.cache_data
def load_table(filename: str) -> pd.DataFrame | None:
    path = TABLES_DIR / filename
    if not path.exists():
        return None
    return pd.read_csv(path)


def show_figure(filename: str, caption: str) -> None:
    path = FIGURES_DIR / filename
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Missing figure: {filename}")


def finding_card(title: str, body: str) -> None:
    st.markdown(
        f"""
<div class="finding-card">
    <div class="finding-title">{title}</div>
    <div class="finding-body">{body}</div>
</div>
""",
        unsafe_allow_html=True,
    )


st.sidebar.title("scRNAseq Immune Atlas")
st.sidebar.markdown(
    """
A single-cell RNA-seq analysis of immune remodeling in inflammatory bowel disease.

**Focus:** immune-cell compartment  
**Disease context:** IBD intestinal tissue  
**Main result:** inflammatory macrophage programs in inflamed tissue
"""
)

page = st.sidebar.radio(
    "Navigate",
    [
        "Project Summary",
        "Key Figures",
        "Result Tables",
        "Methods",
        "Interpretation",
    ],
)

st.markdown('<div class="main-title">scRNAseq Immune Atlas</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Single-cell RNA-seq analysis of immune remodeling in inflammatory bowel disease</div>',
    unsafe_allow_html=True,
)


if page == "Project Summary":
    st.markdown('<div class="section-header">Project Summary</div>', unsafe_allow_html=True)

    st.markdown(
        """
This dashboard presents results from a single-cell RNA-seq analysis of immune cells from
healthy, non-inflamed, and inflamed intestinal tissue. The analysis focuses on immune cell
composition, marker gene validation, macrophage disease-associated expression, and pathway
enrichment.
"""
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
<div class="metric-card">
<b>Tissue conditions</b><br>
Healthy, non-inflamed, inflamed
</div>
""",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
<div class="metric-card">
<b>Main cell type focus</b><br>
Macrophages
</div>
""",
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
<div class="metric-card">
<b>Main biological signal</b><br>
Inflammatory myeloid activation
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown('<div class="section-header">Core Questions</div>', unsafe_allow_html=True)

    q1, q2 = st.columns(2)
    with q1:
        finding_card(
            "Immune composition",
            "Which immune cell populations are present, and how do their proportions differ across tissue conditions?",
        )
        finding_card(
            "Marker validation",
            "Do annotated immune clusters express expected canonical marker genes?",
        )

    with q2:
        finding_card(
            "Disease expression",
            "Which macrophage genes are associated with inflamed intestinal tissue?",
        )
        finding_card(
            "Pathway enrichment",
            "Which biological processes are enriched among genes upregulated in inflamed macrophages?",
        )

    st.markdown("---")
    st.markdown('<div class="section-header">Analysis Workflow</div>', unsafe_allow_html=True)

    st.markdown(
        """
1. Load immune-cell expression matrix and metadata  
2. Create a Scanpy `AnnData` object  
3. Compare immune cell composition across tissue conditions  
4. Validate immune cluster identities using marker genes  
5. Compare macrophage expression between inflamed and healthy tissue  
6. Interpret upregulated genes using Gene Ontology enrichment  
"""
    )


elif page == "Key Figures":
    st.markdown('<div class="section-header">Key Figures</div>', unsafe_allow_html=True)

    selected_figure = st.selectbox("Choose a figure", list(FIGURES.keys()))
    fig_info = FIGURES[selected_figure]

    st.subheader(selected_figure)
    show_figure(fig_info["file"], fig_info["caption"])

    st.markdown("---")

    if selected_figure == "Immune composition":
        st.markdown(
            """
**Finding:** Immune cell composition differs across healthy, non-inflamed, and inflamed intestinal tissue.
This supports the presence of condition-associated immune remodeling in IBD tissue.
"""
        )

    elif selected_figure == "Canonical marker validation":
        st.markdown(
            """
**Finding:** Canonical marker genes support the major immune cluster annotations, including T cells,
regulatory T cells, B/plasma cells, myeloid cells, and mast cells.
"""
        )

    elif selected_figure == "Macrophage inflammatory genes":
        st.markdown(
            """
**Finding:** Inflamed macrophages show stronger expression of inflammatory myeloid genes such as
`S100A8`, `S100A9`, `S100A6`, and `LYZ`.
"""
        )

    elif selected_figure == "Macrophage pathway enrichment":
        st.markdown(
            """
**Finding:** Genes upregulated in inflamed macrophages are enriched for cytokine response,
cytokine production, TNF regulation, inflammatory response, and innate immune defense programs.
"""
        )


elif page == "Result Tables":
    st.markdown('<div class="section-header">Result Tables</div>', unsafe_allow_html=True)

    selected_table_label = st.selectbox("Choose a result table", list(TABLES.keys()))
    selected_table_file = TABLES[selected_table_label]
    df = load_table(selected_table_file)

    st.markdown(f"**Selected table:** `{selected_table_file}`")

    if df is None:
        st.warning(f"Missing table: {selected_table_file}")
    else:
        st.dataframe(df, use_container_width=True, height=520)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=selected_table_file,
            mime="text/csv",
        )

        st.markdown(
            f'<div class="small-note">Rows: {df.shape[0]} | Columns: {df.shape[1]}</div>',
            unsafe_allow_html=True,
        )


elif page == "Methods":
    st.markdown('<div class="section-header">Methods</div>', unsafe_allow_html=True)

    st.markdown(
        """
### Data structure

The analysis uses the immune-cell compartment from a public inflammatory bowel disease
single-cell RNA-seq dataset. Raw matrix, barcode, gene, and metadata files are combined into
a Scanpy `AnnData` object.

### Composition analysis

Immune cluster counts are converted to percentages within each tissue condition so that
healthy, non-inflamed, and inflamed samples can be compared despite differing total cell counts.

### Marker gene analysis

Cluster marker genes are identified using Scanpy's `rank_genes_groups` function with the
Wilcoxon rank-sum test. Canonical marker genes are then used to validate broad immune identities.

### Disease-associated expression

Macrophages are selected for initial disease-associated expression analysis because myeloid
cells are central mediators of intestinal inflammation. Inflamed macrophages are compared
against healthy macrophages.

### Pathway enrichment

Genes upregulated in inflamed macrophages are tested for Gene Ontology Biological Process
enrichment using `gseapy`. Broad ribosomal, mitochondrial, and non-coding RNA genes are filtered
before the primary biological interpretation.
"""
    )


elif page == "Interpretation":
    st.markdown('<div class="section-header">Biological Interpretation</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        finding_card(
            "Immune remodeling",
            "Immune cell composition differs across healthy, non-inflamed, and inflamed tissue, indicating condition-associated immune remodeling in IBD.",
        )

        finding_card(
            "Cluster validation",
            "Canonical markers support the annotation of major immune populations, including T cells, Tregs, B/plasma cells, myeloid cells, and mast cells.",
        )

    with c2:
        finding_card(
            "Macrophage activation",
            "Inflamed macrophages show increased inflammatory myeloid gene expression, including S100A8, S100A9, S100A6, and LYZ.",
        )

        finding_card(
            "Pathway-level signal",
            "Pathway enrichment supports cytokine response, cytokine production, TNF regulation, inflammatory response, and innate immune defense programs.",
        )

    st.markdown("---")

    st.markdown(
        """
### Overall conclusion

The analysis supports the presence of inflammatory macrophage transcriptional programs in
IBD-associated inflamed intestinal tissue. Composition analysis, marker gene validation,
differential expression, and pathway enrichment together point toward macrophage states
associated with cytokine responsiveness, inflammatory signaling, and innate immune defense.

### Important limitation

The current differential expression analysis is cell-level and exploratory. A future version
should use donor-aware pseudobulk differential expression to improve statistical robustness.
"""
    )