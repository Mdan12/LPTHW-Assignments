#imports sys module into the code.
from sys import argv

#gives argv 2 arguments, also uses argv to get a filename.
script, filename = argv

txt = open(filename)
#prints Here's your file (name of the file  you typed in PowerShell when )
print(f"Here's your file {filename}")
#prints the text inside of the file that was previously opened.
print(txt.read())
#prints Type the filename again:
print("Type the filename again:")
#Lets the person type whatever after >(spaccebar)
file_again =  input("> ")
#Makes it so when you've written something it opens the file again that you previously opened
txt_again = close(file_again)
#prints the text from the file that you just opened before.
print(txt_again.read())
