#!/bin/bash
DATE=`date +%c`; 
echo -n "Enter version: "; 
read VER; 
echo -n "Enter changelog snip: "; 
read CHL; 

cat<<LOG>>$1
finfaktura ($VER) unstable; urgency=low

  * $CHL

 -- Havard Dahle <havard@dahle.no> $DATE

LOG

