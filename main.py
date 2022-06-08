#Q2: FIND PALINDOROMIC WORDS IN A TXT FILE, ( SPERATED BY SPACE, MORE THAN ONE LINE )
def main():
    print('WELCOME ')
    fileNameIn= input('please input file name to read from ')

    # outer = input('file to write to ')

    # fileNameOut = open(outer,'w')
    totalPal = 0

    try:
        with open(fileNameIn) as IN:
            cntLine = 1
            lines = IN.readlines()
            for line in lines:
                print("")
                line = line.replace('\n','')

                print("LINE",cntLine,": ",end="")
                allWords = line.split(' ')
                # print(allWords)
                # print(allWords)
                for word in allWords:
                    # print(allWords)
                    word = word.strip()
                    # print(word)

                    flipped = ""
                    lastIndx = int(len(word) - 1 )
                    while lastIndx >=0 :
                        flipped += word[lastIndx]
                        lastIndx -=1

                    # print("flipped", flipped)

                    if flipped.strip().lower() == word.strip().lower():
                        if flipped == '':
                            break
                        print(word,end=" ")
                        totalPal += 1

                cntLine += 1


    except FileNotFoundError:
        print('FILE NOT FOUND!!')

    print("")
    print("total palindromic words ",totalPal)



    # fileNameOut.close()



if __name__ == '__main__':
    main()
