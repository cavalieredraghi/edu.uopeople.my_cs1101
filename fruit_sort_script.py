#preping the files
#had to prefix r for the raw string, as \u is a unicode escape.
InputFile = open(r'C:\Users\bigge\OneDrive\Documents\school work\python\unsorted_fruits.txt', 'r')
OutputFile = open(r'C:\Users\bigge\OneDrive\Documents\school work\python\sortedFruits.txt','w')

#read and pull file into list
Fruits = InputFile.readlines()

#Sort that list
Fruits.sort()
#create a for each loop to print those items in the list to the new file
for fruit in Fruits:
    #It did not like <> so I had to do is not
    if fruit  is not "\n":
        OutputFile.write(fruit)

#close the files

InputFile.close()
OutputFile.close()
    
