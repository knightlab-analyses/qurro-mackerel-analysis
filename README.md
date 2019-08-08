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

See the notebook regarding the exact versions of Qurro and Songbird used in the
notebook -- the notebook was run using versions of these
packages that didn't match with an official release.

## Why is this README so long?
...Sorry about that!
The rest of this README describes the other folders/files in this repository.

## `20190731_MackerelAnalysisOutput/`
This folder just contains the output from the main notebook
(`Mackerel 16S Data Analysis.ipynb`). Due to doing things late at night, I
think all of the files in this folder were actually generated on August 1, 2019
(sorry for any confusion).

### Omitted database files
Two large files have been omitted from this directory:
`gg_13_8_99_otus.qza` and `gg_13_8_99_taxonomy.qza`.
These are just imported versions of the Greengenes
13_8 99% database information. The `gg_13_8_99_otus.qza` file, in particular,
is fairly large -- so for simplicity's sake I've just removed these files.

(The Greengenes 13_8 99% database should be publicly available online; see,
e.g., [this page on the QIIME 2 2019.7 documentation](https://docs.qiime2.org/2019.7/data-resources/)
for a link to the database.)

## `Fig1/`
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

## `negative_control_stats.py`
This is a small script that looks through the annotated taxonomies of all
features present in the negative control samples. It's handy for checking
that certain features are (for the most part) absent from these samples.

This obviously isn't a very formal way of accounting for contamination (in the
main re-analysis notebook we use a sample exclusion cutoff determined by
[KatharoSeq](https://msystems.asm.org/content/3/3/e00218-17.abstract) as
discussed in this dataset's
[corresponding manuscript](https://www.biorxiv.org/content/10.1101/721555v1) --
the dataset's manuscript also describes a hybrid DNA extraction
approach taken to reduce well-to-well contamination -- see
[this paper](https://msystems.asm.org/content/4/4/e00186-19.abstract)),
but it is a quick way to validate that whatever features we investigate in the
manuscript's case study within Qurro probably aren't contaminants.

Here are some examples of using this script to look for certain taxonomy names
in negative control samples (the script accepts one query at a time, and it's
case-insensitive).

```bash
$ ./negative_control_stats.py shewanella
Identified "shewanella" in 174 features' taxonomy annotations.
Identified 503 samples containing at least one of those 174 features.
Of the 78 negative control samples, 1 contain(s) at least one "shewanella"-matching feature.
Negative control samples containing at least one "shewanella"-matching feature:
1) 11721.ep25ul.1000nl.ntc.2

$ ./negative_control_stats.py synechococcales
Identified "synechococcales" in 182 features' taxonomy annotations.
Identified 831 samples containing at least one of those 182 features.
Of the 78 negative control samples, 0 contain(s) at least one "synechococcales"-matching feature.
```
