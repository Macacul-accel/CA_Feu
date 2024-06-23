# Afficher un rectangle dans le terminal

import sys

def line(size):
    o_line = []
    if int(size) > 2:
        for char in range(int(size) - 2):
            o_line.append("-")
        o_line.insert(0, "o")
        o_line.append("o")
    else:
        for i in range(int(size)):
            o_line.append("o")
    return "".join(o_line)

def replace_char(size):
    str_to_change = line(size)
    char_to_change = {"o": "|", "-": " "}
    inbetween = "".join(
        char if char not in char_to_change else char_to_change[char] for char in str_to_change)
    return inbetween

def rectangle(size, nb_line):
    final_form = []
    first_and_last_line = line(size)
    inbetween_line = replace_char(size)
    if int(nb_line) > 2:
        for form in range(int(nb_line) - 2):
            final_form.append(inbetween_line)
        final_form.insert(0, first_and_last_line)
        final_form.append(first_and_last_line)
    else:
        for x in range(int(nb_line)):
            final_form.append(first_and_last_line)
    for j in final_form:
        print(j)

try:
    size = sys.argv[1]
    nb_line = sys.argv[2]
    if len(sys.argv) != 2:
        if int(size) < 1 and int(nb_line) < 1:
            sys.exit()
        else:
            rectangle(size, nb_line)
except:
    print("You must put only two numbers higher than 1")
    sys.exit()
