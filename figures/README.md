# Qurro paper figures
## `raw-jsons/`
This directory includes the Vega-Lite JSON specs output from various Qurro
plots. In particular, the JSONs that start with `10_` are from the Top 10% :
Bottom 10% log-ratio, and the other JSONs are from the Shewanella :
Synechococcales log-ratio.

## `biggify.py`, `output_template.html`, and `htmls-with-pretty-figures/`
`biggify.py` is a Python 3 script that goes through `raw-jsons/` and alters
each Vega-Lite JSON spec in various ways (decreasing the numbers of ticks,
increasing font sizes, etc.) in order to make the plots described by these specs
more readable in the Qurro paper.
Furthermore, this script will produce an HTML file for each JSON spec in the
`htmls-with-pretty-figures/` directory: this HTML file is based on the contents
of `output_template.html`.

The reason we do things this way is 1) so that we can automate these changes
for arbitrary specs, and 2) so that we can use versions of Vega, Vega-Lite, and
Vega-Embed that roughly match with what Qurro currently uses. (Due to Vega\*
version updates, loading these plots in the Vega Editor produces slightly
different-looking outputs.) Thanks to Dominik Moritz for suggesting this
general idea for working with relatively old versions of Vega\*.

This script adjusts its modifications somewhat based on the name of the
JSON filename -- e.g. files with `rankplot` in their name are modified in a
different way than files with `scatterplot` in their name.

## `pretty-svgs/`
This directory contains the SVG files exported from the HTML files in
`htmls-with-pretty-figures/`. This was done manually (i.e. by me opening up
each figure's HTML file in Firefox version 69.0 on an Xubuntu laptop and
choosing the `Save as SVG` option).

(For some reason, Chromium 76.0.3809.100 on Xubuntu cut off the color field
labels for some of the plots; since Firefox didn't do this, I assume this is a
browser problem. This is why I'm listing out the browser versions here.)

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

## `final-libreoffice-drawings/`
Finally! This directory contains the LibreOffice Draw ODG files produced by
combining all of the output figures (everything in `pretty-svgs/`,
`fig1d.pdf`, and `fig2d.pdf`) into two separate figures: `fig1.odg` and
`fig2.odg`.

This directory also contains the PDF files produced by exporting these ODG
files into PDFs from LibreOffice Draw (using the "lossless compression" option).

## Did you really need to be that detailed? Sheesh.
I mean, probably not, but better safe than sorry.
