#brings in the feature set from argv in sys.
from sys import argv
#How many argument variables the feature has.
script, input_file = argv
#defining what print_all does, the f is the argument.
def print_all(f):
  print(f.read())

#defines what rewind does, seek(0) goes back to the beginning of the file.
def rewind(f):
  f.seek(0)
#defines what print_a_line does, line_count and f are arguments.
def print_a_line(line_count, f):
  print(line_count, f.readline())
#Assigns a task to the argument current_file,
#in this case it's the result of open(input_file)
current_file = open(argv[1])
#EZ, literally prints the text, \n is not necessary since python already has
#an invisible \n after every print unless something specific is added like end()
print("First let's print the whole file:\n")
#prints the text inside of current_file
print_all(current_file)
#Prints the text
print("Now let's rewind, kind of like a tape.")
#Since print_all(current_file) printed the text from the file it went to the
#end of the file. rewing(current_file) brings the attention back to the start
#of the file.
rewind(current_file)
#prints text
print("Let's print three lines")
#Assigns the number 1 to current_line
current_line = 1
#prints 1 and one line from the file (because of readline())
print_a_line(current_line, current_file)
#prints 2 (Because  current_line is 1 + 1) and then prints the next lines
#Because it already read the first line so therefore it goes right to the next line
current_line = current_line + 1
print_a_line(current_line, current_file)
#prints 3 because current_line went from being 1 to being 2 and now you add + 1
#making it 3. It prints 3 and then the next line from the file, in this case
#it's the last line from the file, but that isn't always the case.
current_line = current_line + 1
print_a_line(current_line, current_file)
