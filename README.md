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
manuscript.

## Jupyter Notebooks
We recommend using [nbviewer](https://nbviewer.jupyter.org/) to view the
notebooks in this repository:

- [**Here's a link to the main notebook**](https://nbviewer.jupyter.org/github/knightlab-analyses/qurro-mackerel-analysis/blob/master/Mackerel%2016S%20Data%20Analysis.ipynb) mentioned at the start of the case study section.

- [**Here's a link to the notebook that produces Figs. 1(d) and 2(d)**](https://nbviewer.jupyter.org/github/knightlab-analyses/qurro-mackerel-analysis/blob/master/figures/ProduceLogRatioToEstAgeRegressions.ipynb), as mentioned in the figure captions.

- [**Here's a link to the sample dropout analysis notebook**](https://nbviewer.jupyter.org/github/knightlab-analyses/qurro-mackerel-analysis/blob/master/figures/ProduceLogRatioToEstAgeRegressions.ipynb) mentioned in section 3 of the supplementary information.

## About the `input/` folder
This folder contains the input data for this analysis notebook (note that SILVA
database files are not included; as the notebook describes, you'll have to
download those yourself if you want to rerun this analysis). This input data
should match the data on Qiita for this study, at least as of November 10,
2019.

## About the `output/` folder
This folder contains most of the output from the main notebook
(`Mackerel 16S Data Analysis.ipynb`).

As you can see from this repository's `.gitignore` file, files in his directory
with names matching the pattern `silva*.qza` are not included; this is because
most of these files are pretty large, and GitHub yelled at me when I tried to
commit them to this repository (so I had to
[do this](https://help.github.com/en/github/managing-large-files/removing-files-from-a-repositorys-history)
and remove these files from the repository + repository history).

### Viewing these artifacts/visualizations
You can view all of the QIIME 2 artifact/visualization files here in
[q2view](https://view.qiime2.org/) by providing a URL of the format
`https://raw.githubusercontent.com/knightlab-analyses/qurro-mackerel-analysis/master/output/songbird-regression-summary.qzv`,
where you can replace `songbird-regression-summary.qzv` with whatever the QZA/QZV file you want to view is named.

Here are some links that'll take you straight to q2view:

 - [Imported feature table summary](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2Foutput%2Ftable-unfiltered-summary.qzv)
 - [Imported and filtered feature table summary](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2Foutput%2Ftable-summary.qzv)
 - [Songbird diagnostic plots](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2Foutput%2Fsongbird-regression-summary.qzv)
 - [Output Qurro plot (uses a development version of Qurro)](https://view.qiime2.org/visualization/?src=https%3A%2F%2Fraw.githubusercontent.com%2Fknightlab-analyses%2Fqurro-mackerel-analysis%2Fmaster%2Foutput%2Fqurro-plot.qzv)

## About the `figures/` folder
Please see the [README in this folder describing the Qurro paper's figures](https://github.com/knightlab-analyses/qurro-mackerel-analysis/tree/master/figures).

## Why did you make this README so long?
Hey, it's not *that* long!
