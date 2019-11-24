#! /usr/bin/env python3
"""
This is a small script that looks through the annotated taxonomies of all
features present in a given sample metadata category.

I threw this together so that I'd have a way of conclusively saying what types
of samples contained or didn't contain Shewanella, Synechococcales, etc.

Based on https://gist.github.com/fedarko/06d432ca873355046738822692937095,
which I actually originally wrote for this analysis -- albeit for a slightly
different purpose.
"""
import biom
import pandas as pd
import click
from qiime2 import Artifact, Metadata
from qurro._df_utils import biom_table_to_sparse_df


@click.command()
@click.option(
    "--table", required=True, help="FeatureTable[Frequency] QZA file"
)
@click.option(
    "--taxonomy", required=True, help="FeatureData[Taxonomy] QZA file"
)
@click.option("--metadata", required=True, help="Sample metadata file")
@click.option(
    "--metadata-column",
    required=True,
    help="Categorical metadata column to separate samples by",
)
@click.option(
    "--taxonomy-query",
    required=True,
    help="String to use for taxonomy searching",
)
def tabulate_presence(
    table: str,
    taxonomy: str,
    metadata: str,
    metadata_column: str,
    taxonomy_query: str,
):

    # Load input files
    tbl_qza = Artifact.load(table)
    tbl = tbl_qza.view(biom.Table)
    tax_qza = Artifact.load(taxonomy)
    tax = tax_qza.view(pd.DataFrame)
    md = Metadata.load(metadata).to_dataframe()

    header = "=" * len(metadata_column)
    print(header)
    print(
        "Table contains: {} samples and {} features.".format(
            *(tbl.shape[::-1])
        )
    )
    print("Taxonomy contains: {} features.".format(len(tax.index)))
    print("Metadata contains: {} samples.".format(len(md.index)))

    # Subset table and metadata to shared sample IDs
    shared_samples = set(tbl.ids()) & set(md.index)
    tbl = tbl.filter(shared_samples)
    # based on https://github.com/biocore/songbird/blob/e988944228edc55d7bf6be00f3724d2bb3d5e86e/songbird/util.py#L161
    md = md.loc[shared_samples]

    # Subset table and taxonomy to shared feature IDs
    shared_features = set(tbl.ids(axis="observation")) & set(tax.index)
    tbl = tbl.filter(shared_features, axis="observation")
    tax = tax.loc[shared_features]

    print(
        "Shared samples: {} (i.e. in both table and metadata)".format(
            len(shared_samples)
        )
    )
    print(
        "Shared features: {} (i.e. in both table and taxonomy)".format(
            len(shared_features)
        )
    )

    tbl_df = biom_table_to_sparse_df(tbl)

    # Identify all features whose taxonomy annotations contain taxonomy_query
    query_features = tax[
        tax["Taxon"].str.lower().str.find(taxonomy_query.lower()) != -1
    ].index
    matching_feature_ct = len(query_features)
    # Yeah, I know this will say "1 features'" if only 1 feature matched, but I
    # don't think it's worth making the code a whole lot uglier to address that
    print(
        'Identified "{}" in {} features\' taxonomy annotations.'.format(
            taxonomy_query, matching_feature_ct
        )
    )

    # If no features matched the query, no reason to go any further down
    if matching_feature_ct == 0:
        quit()

    # Make a copy of the table filtered to just the matching features
    tbl_query = tbl.filter(query_features, axis="observation", inplace=False)

    # Load this filtered table as a pandas SparseDataFrame.
    df_tbl_query = biom_table_to_sparse_df(
        tbl_query, min_row_ct=1, min_col_ct=1
    )

    # 1. Identify each unique category value
    categories = md[metadata_column].unique()
    cat2stats = {}

    print("{}\n{}".format(metadata_column, header))
    # 2. For each category:
    for category in categories:
        # A. Identify all samples belonging to that category
        category_samples = md[md[metadata_column] == category].index

        # B. Identify how many of those samples contain the given tax query
        num_samples_with_match = 0
        for sample_id in category_samples:
            tax_match_features_in_sample = df_tbl_query[
                df_tbl_query[sample_id] > 0
            ].index
            if len(tax_match_features_in_sample) > 0:
                num_samples_with_match += 1
                if category == "sea water":
                    print(sample_id)

        # D. Report stats by unique category value
        pct = (num_samples_with_match / len(category_samples)) * 100
        print(
            "{}: {} / {} samples ({:.2f}%) have at least one '{}' feature".format(
                category,
                num_samples_with_match,
                len(category_samples),
                pct,
                taxonomy_query,
            )
        )


if __name__ == "__main__":
    tabulate_presence()
