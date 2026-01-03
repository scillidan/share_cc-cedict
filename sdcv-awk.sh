#!/bin/bash
# Authors: GPT-4o mini🧙‍♂️, scillidan🤡

awk '
BEGIN { RS=""; FS="\n"; count=0 }  # RS="" means paragraph mode, FS="\n" splits lines
{
  delete filtered_lines
  filtered_count = 0
  for(i=1; i<=NF; i++) {
    line = $i
    # skip lines starting with --> (dict and word headers)
    # skip lines starting with Found ... items
    if(line ~ /^-->/) continue
    if(line ~ /^Found [0-9]+ items, similar to/) continue
    filtered_lines[++filtered_count] = line
  }
  # If after filtering still have lines, print with number
  if(filtered_count > 0) {
    count++
    print count ". " filtered_lines[1]
    for(j=2; j<=filtered_count; j++) {
      print filtered_lines[j]
    }
    print ""
  }
}
'
