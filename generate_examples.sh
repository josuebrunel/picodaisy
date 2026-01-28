#!/bin/bash

mkdir -p examples

variants=("blue" "red" "green" "teal" "light-grey" "dark-grey")

for variant in "${variants[@]}"; do
    echo "Generating examples/${variant}.html..."
    sed "s|href=\"pico-daisy.css\"|href=\"https://cdn.jsdelivr.net/gh/josuebrunel/picodaisy@latest/pico-daisy.${variant}.css\"|g" index.html > "examples/${variant}.html"
done

echo "Examples generated successfully."