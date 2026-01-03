#!/bin/bash
# Authors: GPT-4o mini🧙‍♂️, scillidan🤡

awk '
BEGIN {
  RS="";  # paragraph mode
  FS="\n"; # line splitting
  count=0;
}
{
  start_line = 1
  if ($1 ~ /^From /) {
    start_line = 2
  }
  nlines=0
  delete lines
  for(i=start_line; i<=NF; i++){
    nlines++
    lines[nlines] = $i
  }
  if(nlines == 0) next;

  count++
  number_printed=0
  for(i=1; i<=nlines; i++){
    line = lines[i]
    if(number_printed == 0 && line !~ /^[[:space:]]*$/){
      # Remove leading spaces from the first non-empty line
      sub(/^[ \t]+/, "", line)
      printf "  %d. %s\n", count, line
      number_printed=1
    } else {
      print line
    }
  }
  print ""
}
'
