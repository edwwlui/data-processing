//remove leading and trailing spaces
awk 'BEGIN{FS=OFS="\t"}{gsub(/^[ ]+/,"",$1);gsub(/[ ]+$/,"",$1)}1' phenotypes.txt > phenotypes1.txt
