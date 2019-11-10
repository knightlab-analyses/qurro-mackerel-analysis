# Qurro paper figures
## `raw-jsons/`
This directory includes the Vega-Lite JSON specs output from various Qurro
plots. In particular, the JSONs that start with `10_` are from the Top 10% :
Bottom 10% log-ratio, and the other JSONs are from the Shewanella :
Synechococcales log-ratio.

## `biggify.py`, `output_template.html`, and `htmls-with-pretty-figures/`
This Python 3 script goes through `raw-jsons/` and alters the Vega-Lite JSON
specs in various ways (decreasing the numbers of ticks, increasing font sizes,
etc.) in order to make these plots more readable in the Qurro paper.
Furthermore, it'll produce an HTML file for each JSON spec in the
`htmls-with-pretty-figures/` directory: this HTML file is based on the contents
of `output_template.html`.

This script adjusts its modifications somewhat based on the name of the
JSON filename -- e.g. files with `rankplot` in their name are modified in a
different way than files with `scatterplot` in their name.

## `final-svgs/`
This directory contains the SVG files exported from the HTML files in
`htmls-with-pretty-figures/`. This was done manually (i.e. by me opening up
each HTML file in Chromium and **TODO**).

## `logratios.tsv` and `10_logratios.tsv`
These files contain data exported from the sample plot. In particular, both
files were exported while the scatterplot had its x-axis field set to `age_2`
and its color field set ot `sample_type_body_site`.
As with the JSONs described above, the TSV file that starts with `10_` was
exported while the Top 10% : Bottom 10% log-ratio was selected, and the
other TSV file was exported while the Shewanella : Synechococcales log-ratio
was selected.

## `ProduceLogRatioToEstAgeRegressions.ipynb`, `fig1d.pdf`, and `fig2d.pdf`
The Jupyter Notebook uses the aforementioned `logratios.tsv` and
`10_logratios.tsv` files to produce `fig1d.pdf` and `fig2d.pdf`, respectively.
Please read the notebook for more details.
