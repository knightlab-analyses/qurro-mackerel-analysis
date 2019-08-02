# qurro-mackerel-analysis
The Jupyter notebook in this repository performs a simple re-analysis of
mackerel and environmental sample 16S data
([Qiita study ID 11721](https://qiita.ucsd.edu/study/description/11721)) in
[QIIME 2](https://qiime2.org/),
[Songbird](https://github.com/biocore/songbird/),
and [Qurro](https://github.com/biocore/qurro/). This is for the Qurro
manuscript, which is in preparation.

The analysis is done in the `Mackerel 16S Data Analysis.ipynb` Jupyter
Notebook. We recommend using nbviewer to view the notebook
([here's a link to the notebook on nbviewer](https://nbviewer.jupyter.org/github/knightlab-analyses/qurro-mackerel-analysis/blob/master/Mackerel%2016S%20Data%20Analysis.ipynb)).

## `negative_control_stats.py`
This is a small script that looks through the annotated taxonomies of all
features present in the negative control samples. It's handy for checking
that certain features are (for the most part) absent from these samples.

This obviously isn't a very formal way of accounting for contamination (in the
re-analysis notebook we use a sample exclusion cutoff determined by
[KatharoSeq](https://msystems.asm.org/content/3/3/e00218-17.abstract)),
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

$ ./negative_control_stats.py alphaproteobacteria
Identified "alphaproteobacteria" in 3652 features' taxonomy annotations.
Identified 1106 samples containing at least one of those 3652 features.
Of the 78 negative control samples, 22 contain(s) at least one "alphaproteobacteria"-matching feature.
Negative control samples containing at least one "alphaproteobacteria"-matching feature:
1) 11721.GI.DNAntc3
2) 11721.echo5ul.200nlelutionb.1
3) 11721.ep25ul.1000nl.sigmah20.1
4) 11721.echo5ul.200nlsigmah20.6
5) 11721.fishP1.ntc.8
6) 11721.ep25ul.1000nl.elutionb.7
7) 11721.echo5ul.200nlsigmah20.1
8) 11721.fishP2.ntc.3
9) 11721.fishP2.ntc.2
10) 11721.ep25ul.1000nl.ntc.2
11) 11721.fishP2.ntc.6
12) 11721.echo5ul.200nlelutionb.7
13) 11721.inv.ntc.6
14) 11721.fishP2.ntc.8
15) 11721.inv.ntc.5
16) 11721.ep25ul.1000nl.sigmah20.8
17) 11721.echo5ul.200nlntc.3
18) 11721.echo5ul.200nlsigmah20.5
19) 11721.inv.ntc.4
20) 11721.ep25ul.1000nl.sigmah20.4
21) 11721.echo5ul.200nlelutionb.4
22) 11721.fishP1.ntc.1
```

## Note re: database files
Two large files have been omitted from the `20190731_MackerelAnalysisOutput`
directory in this repository: `gg_13_8_99_otus.qza` and
`gg_13_8_99_taxonomy.qza`. These are just imported versions of the Greengenes
13_8 99% database information. The `gg_13_8_99_otus.qza` file, in particular,
is fairly large -- so for simplicity's sake I've just removed these files.

(The Greengenes 13_8 99% database should be publicly available online; see,
e.g., [this page on the QIIME 2 2019.7 documentation](https://docs.qiime2.org/2019.7/data-resources/)
for a link to the database.)
