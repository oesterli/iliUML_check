# iliUML_check
iliUML_checker

branche "test":
-> Log file added

This python script is for:
reading an UML-Editor-file (.uml) for INTERLIS data modelling (https://www.interlis.ch/downloads/umleditor)
deleting duplicated lines in the -uml-file
The script cheks if two consectutive lines start with the same text pattern and deletes than the first of the two lines.
The input file (inFile) must be placed inside the "data" directory In the code you have to define which text pattern shall be checked
The output file (outFile) is written to the "data" directory
