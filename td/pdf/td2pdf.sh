n=1
while read i; do 
  printf -v j "%04d" $n
  wkhtmltopdf --page-size A4 --javascript-delay 5000 --margin-top 0.75in --margin-right 0.75in --margin-bottom 0.75in --margin-left 0.75in --encoding UTF-8 "$i" "$j.pdf";
  n=$((n+1))
done < url-list.txt
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile=bloc4-td.pdf $(ls -1 *.pdf)