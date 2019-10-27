# qurro-mackerel-analysis

## What is this repository?

This main Jupyter notebook in this repository (`Mackerel 16S Data Analysis.ipynb`)
performs a simple re-analysis of mackerel and environmental sample 16S data
([Qiita study ID 11721](https://qiita.ucsd.edu/study/description/11721),
and described in
[Minich et al. 2019](https://www.biorxiv.org/content/10.1101/721555v1)) in
[QIIME 2](https://qiime2.org/),
[Songbird](https://github.com/biocore/songbird/),
and [Qurro](https://github.com/biocore/qurro/). This is for the Qurro
manuscript, which is in preparation.

We recommend using nbviewer to view the notebooks in this repository
([**here's a link to the main notebook**](https://nbviewer.jupyter.org/github/knightlab-analyses/qurro-mackerel-analysis/blob/master/Mackerel%2016S%20Data%20Analysis.ipynb), and [**here's a link to the Fig. 1(d) notebook**](https://nbviewer.jupyter.org/github/knightlab-analyses/qurro-mackerel-analysis/blob/master/Fig1/Fig1d/ProduceFig1d.ipynb)).

## What are the system requirements for the notebooks/code in this repository?
The main analysis notebook assumes the presence of various files on the current
system (it was ran on Barnacle, [a cluster used by our lab](https://knightlab.ucsd.edu/wordpress/wp-content/uploads/2016/04/Knight-Lab-Facilities-Resources-and-Equipment.pdf)). If you'd like to rerun this notebook yourself, you can just modify the
environment variables declared in **section 0.1** of the notebook to match the
locations of files on your system.

Furthermore, it's assumed that:

- you are within a QIIME 2 conda environment (of a QIIME 2 version >= 2019.7).
- Qurro is installed
- Songbird is installed

See the notebook regarding the exact versions of the QIIME 2 plugins (including
Qurro and Songbird) used in this analysis.

## Why is this README so long?
...Sorry about that!
The rest of this README describes the other folders/files in this repository.

## `AnalysisOutput/`
This folder just contains the output from the main notebook
(`Mackerel 16S Data Analysis.ipynb`).

## `Fig1/`
**NOTE: The figures in this folder are out of date. I need to redo these now
that I redid the analysis.**
This folder contains `final.odg`, a
[LibreOffice Draw](https://www.libreoffice.org/discover/draw/) file I used to
create Figure 1. (For the most part, I just stitched together the input SVG/PDF
files, added the Shewanella and Synechococcales labels to the rank plot, and
added labels like "(a)".)

This folder also contains `final.pdf`, which is just the exported version of
`final.odg`.

### `Fig1abc/`
This folder contains exported versions of the rank plot, sample plot (boxplot),
and sample plot (scatterplot, using `age_2` as the x-axis) from a Qurro
visualization of the mackerel dataset (using the Songbird differentials
computed in the main analysis notebook in this repository). These exported
versions have been edited in the [Vega Editor](https://vega.github.io/editor)
to make them more suitable for display (e.g. title font sizes increased, less
axis ticks used, certain axes renamed to a more human-readable explanation,
...)

### `Fig1d/`
The Jupyter notebook in this folder (`ProduceFig1d.ipynb`)
uses exported data from the Qurro visualization
generated in the analysis (`g_shew_over_o_syn_age.tsv`) as the starting point
for performing linear regression to evaluate the correlation between estimated
fish age and the *Shewanella*:*Synechococcales* log-ratio.
