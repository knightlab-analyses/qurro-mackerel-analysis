#! /usr/bin/env python3
import sys
import os
import biom
import pandas as pd
from qiime2 import Artifact, Metadata
from qurro._df_utils import biom_table_to_sparse_df

OUT_DIR = "20190726_MackerelAnalysisOutput"
TABLE_QZA_FILEPATH = os.path.join(OUT_DIR, "table-unfiltered.qza")
TAXONOMY_QZA_FILEPATH = os.path.join(OUT_DIR, "taxonomy.qza")
METADATA_FILEPATH = os.path.join(OUT_DIR, "metadata.tsv")

try:
    tax_query = sys.argv[1]
except IndexError:
    raise ValueError(
        "You need to specify some text to use for searching taxonomy!"
    )

# Load the table
tbl_qza = Artifact.load(TABLE_QZA_FILEPATH)
tbl = tbl_qza.view(biom.Table)

# Load the taxonomy
tax_qza = Artifact.load(TAXONOMY_QZA_FILEPATH)
tax = tax_qza.view(pd.DataFrame)

# Load the sample metadata
md = Metadata.load(METADATA_FILEPATH).to_dataframe()

# Identify negative control samples: that is, all samples where
# empo_1 == "control" and empo_2 == "negative".
c_sample_md = md[md["empo_1"] == "control"]
n_c_samples = c_sample_md[c_sample_md["empo_2"] == "negative"].index

# Identify all features whose taxonomy annotations contain tax_query
query_features = tax[tax["Taxon"].str.find(tax_query) != -1].index
print(
    'Identified "{}" in {} features\' taxonomy annotations.'.format(
        tax_query, len(query_features)
    )
)

# Make a copy of the table filtered to just the features matching tax_query
tbl_query = tbl.filter(query_features, axis="observation", inplace=False)

# Load this filtered table as a pandas SparseDataFrame.
df_tbl_query = biom_table_to_sparse_df(tbl_query, min_row_ct=1, min_col_ct=1)

# Find all samples containing at least one count of a "Shewanella feature"
samples_with_query = df_tbl_query.columns[df_tbl_query.sum(axis="index") > 0]
print(
    "Identified {} samples containing at least one of those {} "
    "features.".format(len(samples_with_query), len(query_features))
)

# ...Filter this to just *negative control* samples
n_c_samples_with_query = set(samples_with_query) & set(n_c_samples)
print(
    "Of the {} negative control samples, {} contain(s) at least one "
    '"{}"-matching feature.'.format(
        len(n_c_samples), len(n_c_samples_with_query), tax_query
    )
)

if len(n_c_samples_with_query) > 0:
    print('"{}"-matching features:'.format(tax_query))
    print(n_c_samples_with_query)
