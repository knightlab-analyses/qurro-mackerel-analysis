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

### Viewing these artifacts/visualizations
You can view all of the QIIME 2 artifact/visualization files here in
[q2view](https://view.qiime2.org/) by providing a URL of the format
`https://raw.githubusercontent.com/knightlab-analyses/qurro-mackerel-analysis/master/AnalysisOutput/songbird-regression-summary.qzv`,
where you can replace `songbird-regression-summary.qzv` with whatever the QZA/QZV file you want to view is named.

Examples that'll take you straight to q2view:

 - [Imported feature table summary](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2FAnalysisOutput%2Ftable-unfiltered-summary.qzv)
 - [Imported and filtered feature table summary](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2FAnalysisOutput%2Ftable-summary.qzv)
 - [Songbird diagnostic plots](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2FAnalysisOutput%2Fsongbird-regression-summary.qzv)
 - [Output Qurro plot (uses a development version of Qurro)](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2FAnalysisOutput%2Fqurro-plot.qzv)

## `figures`
Please see the [README describing the Qurro paper's figures](https://github.com/knightlab-analyses/qurro-mackerel-analysis/tree/master/figures).
