import sys

# Fonctions

def split_expression(input_arg):
    parsed_array = []
    suite = input_arg.split()
    for x in suite:
        if x.isdigit():
            parsed_array.append(int(x))
        else:
            if len(x) != 1:
                if x[0].isdigit():
                    parsed_array.append(int(x[:-1]))
                    parsed_array.append(x[-1])
                else:
                    parsed_array.append(x[0])
                    parsed_array.append(int(x[1:]))
            else:
                parsed_array.append(x)
    return parsed_array

def calcul(splitted_args):
    priority_operator = ["*", "/", "%"]
    temporary_result = []
    parenthesis_result = []
    result = splitted_args

    def cleaning_array(index, array):
        array.pop(index + 1)
        array.pop(index)
        array.pop(index - 1)

    while "(" in result:
        if not "(" in result:
            break
        first_parenthesis_index = result.index("(")
        last_parenthesis_index = result.index(")")
        for parenthesis_args in result[first_parenthesis_index + 1: last_parenthesis_index]:
            parenthesis_result.append(parenthesis_args)
        result.insert(first_parenthesis_index, int(calcul(result[first_parenthesis_index + 1: last_parenthesis_index])))
        for args_in_parenthesis in range(len(parenthesis_result) + 2):
            result.pop(first_parenthesis_index + 1)
    else:
        while priority_operator[0] in result or priority_operator[1] in result or priority_operator[2] in result:
            for operator in result:
                if operator in priority_operator:
                    if operator == "*":
                        operator_index = result.index(operator)
                        temporary_result.append(int(result[operator_index - 1]) * int(result[operator_index + 1]))
                        cleaning_array(operator_index, result)
                        result.insert(operator_index - 1, int(temporary_result[0]))
                        temporary_result.pop(0)
                    elif operator == "/":
                        operator_index = result.index(operator)
                        temporary_result.append(int(result[operator_index - 1]) / int(result[operator_index + 1]))
                        cleaning_array(operator_index, result)
                        result.insert(operator_index - 1, int(temporary_result[0]))
                        temporary_result.pop(0)
                    elif operator == "%":
                        operator_index = result.index(operator)
                        temporary_result.append(int(result[operator_index - 1]) % int(result[operator_index + 1]))
                        cleaning_array(operator_index, result)
                        result.insert(operator_index - 1, int(temporary_result[0]))
                        temporary_result.pop(0)
    
    while len(result) != 1:
        if len(result) == 1:
            break
        not_priority_ope = 1
        if result[not_priority_ope] == "+":
            temporary_result.append(int(result[not_priority_ope - 1]) + int(result[not_priority_ope + 1]))
            cleaning_array(not_priority_ope, result)
            result.insert(not_priority_ope - 1, int(temporary_result[0]))
            temporary_result.pop(0)
        elif result[not_priority_ope] == "-":
            temporary_result.append(int(result[not_priority_ope - 1]) - int(result[not_priority_ope + 1]))
            cleaning_array(not_priority_ope, result)
            result.insert(not_priority_ope - 1, int(temporary_result[0]))
            temporary_result.pop(0)

    return result[0]


# Error

if len(sys.argv) != 2:
    print("Only one argument")
    sys.exit()
for elmt in sys.argv[1]:
    if elmt in map(chr, range(97, 123)) or elmt in map(chr, range(65, 91)):
        print("Don't put letters")
        sys.exit()

# Parsing

expression = sys.argv[1]

# Résolution

splitted_array = split_expression(expression)
final_result = calcul(splitted_array)

# Affichage

print(final_result)