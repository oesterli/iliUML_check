# -*- coding: utf-8 -*-


# Open files
outFile = open("data/seismic/DM_2D-Seismic_190702_mod.uml", "w")
log = open("data/seismic/log.tsv", "w")

# Define Variables
line_A = 'emptyLine_A'
line_A = 'emptyLine_B'
i = 1
count = 0
regex = '<Entry TID='
log.write('LineNum' + '\t' + 'ActionType' + '\t' + 'lineString' + '\t' + 'CurrentCount' + '\n')

with open('data/seismic/DM_2D-Seismic_190702_orig.uml') as inFile:
    for line in inFile:
        # If the current line starts with the string defined in "regex" do the following
        if line.startswith(regex):
            firstLine = line
            secondLine = next(inFile)

            # If the consecutive line starts with the string defined in "regex" do the following
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

                # Write to log-file
                count += 1
                log.write(str(i) + '\t' + 'First line deleted.' + '\t' + firstLine + '\t' + str(count) + '\n')
                i += 2

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
                # count += 1
                # log.write('First line written. Current count: ' + str(count) + '\n')
                outFile.write(secondLine)
                # count += 1
                # log.write('Second line written. Current count: ' + str(count) + '\n')
                i += 2
        else:
            ######
            # TESTING: Write each line to outFile
            #outFile.write(str(i) + ' LINE ' + line)

            # Create line numbe
            #i += 1
            ######

            # PRODUCTIVE: Write line to outFile
            outFile.write(line)
            # count += 1
            # log.write('Line. Current count: ' + str(count) + '\n')
            i += 1



# Write log-file
log.write('-----------------------------------\n'
          'Total count of actions: ' + str(count) +
          '\n-----------------------------------')


# Close inFile and outFile
inFile.close()
outFile.close()
log.close()
