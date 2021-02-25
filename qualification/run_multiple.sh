#!/bin/bash

if [ $# -eq 0 ]
then
    # If no arguments provided, run all
    all_inputs="a b c d e f"
else
    all_inputs="$@"
fi

echo "Selected inputs: $all_inputs"

for input in $(echo "$all_inputs")
do
    echo "> Running: $input";
    python solution.py "$input"
    echo "----------";
done
