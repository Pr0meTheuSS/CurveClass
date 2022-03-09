import numpy as np
import random
import string


def RandSpaces():
    # * random.randint(0, 5)
    return " "


def GetUniqueTokens(quadratic_form: str) -> list:
    # Allowable tokens in string
    tokens_list = ['+', '-', '^', '*', ' ', '.', ',']
    # List of customer's variable's names
    unique_tokens_list = []
    # Collect unique tokens ~ customer's variable's names
    for ch in quadratic_form:
        if ch not in tokens_list and not ch.isdigit() and ch not in unique_tokens_list:
            unique_tokens_list.append(ch)
            # Assert that quadratic form is double function (for example -  f(x,y)) with two variable's names
            if len(unique_tokens_list) > 2:
                return []
    return unique_tokens_list


def GetNumber(number: str) -> float:
    if number == '-':
        return -1.0
    if number == '':
        return 0.0
    elif '-' in number:
        return -float(number.replace('-', ''))
    else:
        return float(number)


def GetTermsList(quadratic_form: str, variables: list) -> list:
    # Delete all multiplication tokens and spaces
    quadratic_form = quadratic_form.translate({ord(' '): '', ord('*'): ''})
    print("Quadratic form is: {forms}", quadratic_form)
    # Replace 'yx' to 'xy'
    quadratic_form = quadratic_form.replace(variables[1] + variables[0], variables[0] + variables[1])
    # Replace 'x^2' to 'xx' and 'y^2' to 'yy'
    for var in variables:
        quadratic_form = quadratic_form.replace(var + "^2", var * 2)
    # Replace '-...' to '+-...' for split by '+' symbol
    print("Quadratic form is: {forms}", quadratic_form)
    quadratic_form = quadratic_form.replace('-', '+-')
    quadratic_form = quadratic_form.replace('++', '+')
    print("Quadratic form is: {forms}", quadratic_form)

    return quadratic_form.split('+')


def ParseCoefficient(quadratic_form: str) -> np.array:
    """
    :rtype: object
    """
    variables = GetUniqueTokens(quadratic_form)
    assert(len(variables) == 2)
    # Empty coefficient matrix to return
    coeff_matrix = np.array([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]
                             ])
    terms_list = GetTermsList(quadratic_form, variables)
    var_perm = {variables[0] * 2: [(0, 0)],
                variables[0] + variables[1]: [(0, 1), (1, 0)],
                variables[1] * 2: [(1, 1)],
                variables[0]: [(0, 2), (2, 0)],
                variables[1]: [(1, 2), (2, 1)],
                'free_value': [(2, 2)]
                }
    print(terms_list)
    for term in terms_list:
        if variables[0] + variables[1] in term:
            literal_part = variables[0] + variables[1]
        elif variables[0] * 2 in term:
            literal_part = variables[0] * 2
        elif variables[1] * 2 in term:
            literal_part = variables[1] * 2
        elif variables[0] in term:
            literal_part = variables[0]
        elif variables[1] in term:
            literal_part = variables[1]
        else:
            literal_part = 'free_value'
        formatted_term = term.replace(literal_part, '')
        for pos in var_perm[literal_part]:
            coeff_matrix[pos[0]][pos[1]] = GetNumber(formatted_term)
    return coeff_matrix


def CreateValidTestForParser(c_matrix: np.array) -> str:
    # Generate random variable's names
    print(c_matrix)
    var_names = [random.choice(string.ascii_letters), random.choice(string.ascii_letters)]
    print(var_names)
    # If names are the same
    while var_names[1] == var_names[0]:
        var_names[1] = random.choice(string.ascii_letters)
    term_list = []
    # Generate second-order terms
    for i in range(2):
        term_list.append(str(c_matrix[i][i]) + var_names[i] + "^" + RandSpaces() + "2")
    assert(c_matrix[0][1] == c_matrix[1][0])
    var_names_perm = var_names
    random.shuffle(var_names_perm)
    term_list.append(str(c_matrix[0][1]) + var_names_perm[0] + RandSpaces() + var_names_perm[1])
    # Generate first-order terms
    assert(c_matrix[0][2] == c_matrix[2][0])
    assert(c_matrix[1][2] == c_matrix[2][1])
    for i in range(2):
        term_list.append(str(c_matrix[i][2]) + RandSpaces() + var_names[i])
    # Generate free value
    term_list.append(RandSpaces() + str(c_matrix[2][2]))
    random.shuffle(term_list)
    return "+".join(term_list)


if __name__ == '__main__':
    # Generate random array 3x3
    c_matrix = np.random.randint(-1000, 1000, size=(3, 3))
    for i in range(len(c_matrix)):
        for j in range(len(c_matrix[0])):
            c_matrix[i][j] = c_matrix[j][i]
    print(c_matrix)

    test_in = CreateValidTestForParser(c_matrix)
    print(test_in)
    print(ParseCoefficient(test_in))
