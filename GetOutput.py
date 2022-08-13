dictOFSummarys = {}

def summary(n):
    f = open(f"./TEXT/Document{n}.txt", encoding="utf-8")

    dictOFSummaryPerPaper = {}
    words = []

    for line in f:
        for word in line.split():
            words.append(word) # make a list of words

    for i in range (len(words)):
        tempAbs, tempExs = "", ""
        if words[i] == 'Table': # scan for the word 'Table'
            try:
                tableNumber = int(words[i+1][0]) # scan the number of the table
            except:
                continue

            if tableNumber not in dictOFSummaryPerPaper.keys():
                dictOFSummaryPerPaper[tableNumber] = {'Abstractive': "", 'Extractive': ""}

            if words[i+1][-1] == ':': # check ':' for abstractive summary
                try:
                    while words[i - 1][-1] != '.': # stop when we get a fullstop
                        tempAbs = tempAbs + ' ' + words[i]
                        i = i + 1
                except:
                    continue

                dictOFSummaryPerPaper[tableNumber]['Abstractive'] += tempAbs # insert the line in dictionary
                tempAbs = ""
            else: # else it is a extractive summary
                countOfFullStop, index = 0, i
                while (countOfFullStop != 2): # scan for 2nd fullstop as we need a sentence before the 'Table' sentence
                    if words[index][-1] == '.':
                        countOfFullStop += 1
                    index -= 1

                countOfFullStop = 0
                index += 2

                while (countOfFullStop != 3): # we need 3 lines - sentence before 'Table' + sentence with 'Table' + sentence after 'Table'
                    tempExs = tempExs + ' ' + words[index]
                    try:
                        if (words[index][-1] == '.'):
                            countOfFullStop += 1
                        index += 1
                    except:
                        continue

                i = index
                dictOFSummaryPerPaper[tableNumber]['Extractive'] += tempExs # insert these lines in dictionary
                tempExs = ""

    dictOFSummarys[n] = dictOFSummaryPerPaper # insert the dictionary into another dictionary
    f.close()

def abstractExtractor():
    for i in range (1, 1364):
        try:
            summary(i)
        except:
            continue

    toWrite = ""
    f = open('Output.txt', 'x', encoding='utf-8')
    f.close()
    for i in dictOFSummarys.keys():
        toWrite = f"<Paper ID = {i}> " # formatting in xml style
        x = dictOFSummarys[i]
        for j in x.keys():
            toWrite += f" <Table ID = {j}> "
            y = x[j]
            for k in y.keys():
                toWrite += f" <{k} Summary> = {y[k]} </{k} Summary> "
            toWrite += f" </Table ID = {j}> "
        toWrite += f" </Paper ID = {i}> "

        f = open('Output.txt', 'a', encoding='utf-8')
        f.write(toWrite)
        f.write('\n\n')
        f.close
        toWrite = ""
