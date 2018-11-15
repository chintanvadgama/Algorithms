for fn in `ls -1 *.py`; do
	echo "\n"	
	echo "\n************* $fn **************\n";
	cat $fn;
done > codesamples.txt
