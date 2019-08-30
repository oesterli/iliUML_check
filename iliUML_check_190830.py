# -*- coding: utf-8 -*-


# Open files
outFile = open("data/Asset_CHBase_mod.uml", "w")

# Define Variables
line_A = 'emptyLine_A'
line_A = 'emptyLine_B'
i = 1
regex = '<Entry TID='

with open('data/Asset_CHBase_orig.uml') as inFile:
    for line in inFile:
        if line.startswith(regex):
            firstLine = line
            secondLine = next(inFile)

            if secondLine.startswith(regex):
                ######
                # TESTING: Write each line to outFile
                # outFile.write(str(i) + ' DELETED FIRSTLINE ' + firstLine)
                # outFile.write(str(i+1) + ' SECONDLINE ' + secondLine)

                # Create line numbers
                #i += 2
                ######

                # PRODUCTIVE: Write second line to outFile
                outFile.write(secondLine)

            else:
                ######
                # TESTING: Write each line to outFile
                #outFile.write(str(i) + ' FIRSTLINE' + firstLine)
                #outFile.write(str(i+1) + ' SECONDLINE' + secondLine)

                # Create line numbers
                #i += 2
                ######

                # PRODUCTIVE: Write first and second line to outFile
                outFile.write(firstLine)
                outFile.write(secondLine)
        else:
            ######
            # TESTING: Write each line to outFile
            #outFile.write(str(i) + ' LINE ' + line)

            # Create line numbe
            #i += 1
            ######

            # PRODUCTIVE: Write line to outFile
            outFile.write(line)




# Close inFile and outFile
inFile.close()
outFile.close()