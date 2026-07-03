from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def clean_go_term_labels(terms: pd.Series) -> pd.Series:
    """Remove GO identifiers from Gene Ontology term labels."""
    return terms.str.replace(r"\s*\(GO:\d+\)", "", regex=True)


def plot_go_enrichment_bar(
    enrichment_results: pd.DataFrame,
    output_path: str | Path | None = None,
    n_terms: int = 15,
    title: str = "GO biological processes enriched in inflamed macrophage genes",
):
    """Plot top GO enrichment terms by -log10 adjusted p-value."""
    plot_data = enrichment_results.sort_values("Adjusted P-value").head(n_terms).copy()
    plot_data["neg_log10_adj_p"] = -np.log10(plot_data["Adjusted P-value"])
    plot_data["Term_clean"] = clean_go_term_labels(plot_data["Term"])
    plot_data = plot_data.sort_values("neg_log10_adj_p", ascending=True)

    sns.set_theme(style="whitegrid", context="notebook")

    plt.figure(figsize=(10, 7))

    ax = sns.barplot(
        data=plot_data,
        x="neg_log10_adj_p",
        y="Term_clean",
        hue="neg_log10_adj_p",
        palette="Blues",
        dodge=False,
        legend=False,
    )

    for i, (_, row) in enumerate(plot_data.iterrows()):
        ax.text(
            row["neg_log10_adj_p"] + 0.08,
            i,
            f"FDR={row['Adjusted P-value']:.1e}",
            va="center",
            fontsize=8,
        )

    ax.set_xlabel("-log10 adjusted p-value", fontsize=11)
    ax.set_ylabel("")
    ax.set_title(title, fontsize=13, weight="bold", pad=12)

    ax.grid(axis="x", alpha=0.3)
    ax.grid(axis="y", visible=False)

    sns.despine(left=True, bottom=False)
    plt.xlim(0, plot_data["neg_log10_adj_p"].max() + 1.5)
    plt.tight_layout()

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    plt.show()

    return ax