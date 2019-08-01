# qurro-mackerel-analysis
The Jupyter notebook in this repository performs a re-analysis of mackerel and
environmental sample 16S data
([Qiita study ID 11721](https://qiita.ucsd.edu/study/description/11721)) in
[QIIME 2](https://qiime2.org/),
[Songbird](https://github.com/biocore/songbird/),
and [Qurro](https://github.com/biocore/qurro/). This is for the Qurro
manuscript, which is in preparation.

## Note re: files
Two large files have been omitted from the `20190731_MackerelAnalysisOutput`
directory in this repository:

- `gg_13_8_99_otus.qza` and `gg_13_8_99_taxonomy.qza` are just imported
  versions of the Greengenes 13_8 99% database information. The
  `gg_13_8_99_otus.qza` file, in particular, is fairly large -- so for
  simplicity's sake I've just removed these files.
    - The Greengenes 13_8 99% database should be publicly available online; see,
      e.g., [this page on the QIIME 2 2019.7 documentation](https://docs.qiime2.org/2019.7/data-resources/) for a link to the database.
