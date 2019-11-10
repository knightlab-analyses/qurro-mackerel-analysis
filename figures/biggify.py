#! /usr/bin/env python3
# Converts a directory of JSON files representing Vega-Lite specifications
# ("raw-jsons") to a directory of HTML files with those specifications
# embedded, and with the specs' font sizes, etc. increased and modified to be
# more readable in publications.
#
# This script will output one HTML file for each JSON file (stored in the
# directory "htmls-with-pretty-figures"). Each HTML file will just be a simple
# page containing the embedded (new) Vega-Lite JSON.
#
# This was written for the Qurro paper, but I'm sure it's adaptable to other
# Vega-Lite JSON files.

import json
import os

with open("output_template.html", "r") as template_file_obj:
    template_text = template_file_obj.read()

for json_filepath in os.listdir("raw-jsons"):
    # Load the "raw" (i.e. exported straight from Qurro, or from the Vega
    # Editor from Qurro since I couldn't get Chrome to do the former...) spec.
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    with open(os.path.join("raw-jsons", json_filepath), "r") as json_file_obj:
        spec = json.load(json_file_obj)

    # Actually modify the spec.

    # 1. modifications common to all specs
    # increase title font size
    spec["config"]["title"] = {"fontSize": 24}
    # increase axis labels' font sizes
    spec["config"]["axis"]["titleFontSize"] = 20
    # increase legend font size and allow long legend text
    spec["config"]["legend"] = {
        "labelFontSize": 16,
        "titleFontSize": 16,
        "titleLimit": 20000,
    }
    # increase tick font size
    for axis in ("x", "y"):
        if "axis" in spec["encoding"][axis]:
            spec["encoding"][axis]["axis"]["labelFontSize"] = 16
        else:
            spec["encoding"][axis]["axis"] = {"labelFontSize": 16}

    # 2. modifications for just rank plots
    if "rankplot" in json_filepath:
        # hide ticks/tick labels on x-axis
        spec["encoding"]["x"]["axis"]["ticks"] = False
        spec["encoding"]["x"]["axis"]["labels"] = False
        # set y-axis tick count to 6
        spec["encoding"]["y"]["axis"]["tickCount"] = 6
        # change y-axis title to something easily readable
        spec["encoding"]["y"]["title"] = "Gill Differentials"
        # remove "both" from legend (since there's no overlap in either of
        # these selected log-ratios), and position it at the top-left
        # corner of the plot (with a small offset)
        spec["encoding"]["color"]["legend"] = {
            "values": ["None", "Numerator", "Denominator"],
            "orient": "none",
            "legendX": 10,
            "legendY": 10,
        }

    # 3. modifications for just box plots
    if "boxplot" in json_filepath:
        # hide ticks/tick labels on x-axis
        spec["encoding"]["x"]["axis"]["ticks"] = False
        spec["encoding"]["x"]["axis"]["labels"] = False
        # hide title for x-axis
        # (None should get converted to null when we call json.dumps())
        spec["encoding"]["x"]["axis"]["title"] = None
        # set y-axis tick count to 3
        spec["encoding"]["y"]["axis"]["tickCount"] = 3

    # 4. modifications for just scatter plots
    if "scatterplot" in json_filepath:
        spec["encoding"]["y"]["axis"]["tickCount"] = 3
        spec["encoding"]["x"]["axis"]["tickCount"] = 5
        spec["encoding"]["x"]["title"] = "Estimated fish age (age_2)"

    # Write out the now-modified spec.
    output_html_text = template_text.replace(
        "Figure: {}", "Figure: {}".format(json_filepath)
    )
    output_html_text = output_html_text.replace(
        "SPEC_GOES_HERE = {}", "SPEC_GOES_HERE = {}".format(json.dumps(spec))
    )
    output_filepath = os.path.join("htmls-with-pretty-figures", json_filepath + ".html")
    with open(output_filepath, "w") as output_html_file_obj:
        output_html_file_obj.write(output_html_text)
