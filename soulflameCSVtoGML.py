import csv
import os

def soulflamecsv_to_gml(languageCode = "EN"):

    #Current Directory
    currentdir = os.getcwd() + "\\"
    exportFilePath = currentdir + "soulflameLang.txt"
    readFilePath = currentdir + "soulflamelang.csv"

    #Clear File
    with open(exportFilePath, "w") as exportfile:
        exportfile.write("function lang" + languageCode + "() {\n")

    #New Dictonary
    sectionDict = {}
    linebreakAfterSection = []

    #Open File as Append
    with open(exportFilePath, "a") as exportfile:  

        #Open Lang CSV
        with open(readFilePath, "r") as f:

            #Get All Rows
            csv_read = csv.reader(f, delimiter=',')

            #Loop Througn Rows
            line = 0
            longestKeyLength = 0
            lastKey = ""
            for row in csv_read:

                if (line != 0):
                    
                    #Group into Sections
                    key = row[0]
                    text = row[1]
                    info = row[2]

                    longestKeyLength = max(len(key), longestKeyLength)

                    if (key != ""):

                        #For Line Break
                        lastKey = key

                        if (info != ""):
                            
                            #info as list
                            infolist = info.split(",")
                            infolistasstr = ""
                            for infopoint in infolist:
                                infolistasstr += "\"{}\", ".format(infopoint)

                            #Other Info Included
                            test = sectionDict.get(key, [])
                            test.append("[\"{}\", {}]".format(text, infolistasstr))
                            sectionDict[key] = test

                            
                        else:
                            #Just Text
                            sectionDict[key] = "\"{}\"".format(text)

                    else:
                        #Add Line Break
                        linebreakAfterSection.append(lastKey)

                else:
                    line += 1

            for key in sectionDict:

                #Create GML String
                val = str(sectionDict[key])
                val = val.replace("'[\"", "[\"")
                val = val.replace("]'", "]")
                print(val)

                gmlDictAccessor = "lang[? \"{}\"]".format(key)
                toFormat = "\t{:<" + str(longestKeyLength + 15) + "} = {};\n"
                writeString = toFormat.format(gmlDictAccessor, val)
                #print(writeString)

                #Write To File
                exportfile.write(writeString)

                if (len(linebreakAfterSection) > 0):
                    if (key == linebreakAfterSection[0]):
                        exportfile.write("\n")
                        linebreakAfterSection.pop(0)

        #Close The Function
        exportfile.write("}")
