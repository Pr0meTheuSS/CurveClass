import numpy as np


def GetUniqueTokens(quadratic_form: str) -> list:
    # Allowable tokens in string
    tokens_list = ['+', '-', '^', '*', ' ', '.', ',']
    # List of customer's variable's names
    unique_tokens_list: list[str] = []
    # Collect unique tokens ~ customer's variable's names
    # TODO: change to list generator
    for ch in quadratic_form:
        if ch not in tokens_list and not ch.isdigit() and ch not in unique_tokens_list:
            unique_tokens_list.append(ch)
            # Assert that quadratic form is double function (for example -  f(x,y)) with two variable's names
            if len(unique_tokens_list) > 2:
                return []
    return unique_tokens_list


def GetInt(number: str) -> int:
    if number == '-':
        return -1
    if number == '':
        return 0
    elif '-' in number:
        return -int(number.replace('-', ''), 10)
    else:
        return int(number, 10)


def GetTermsList(quadratic_form: str, variables: list) -> list:
    # Delete all multiplication tokens and spaces
    quadratic_form = quadratic_form.translate({ord(' '): '', ord('*'): ''})
    # Replace 'yx' to 'xy'
    quadratic_form = quadratic_form.replace(variables[1] + variables[0], variables[0] + variables[1])
    # Replace 'x^2' to 'xx' and 'y^2' to 'yy'
    for var in variables:
        quadratic_form = quadratic_form.replace(var + "^2", var * 2)
    # Replace '-...' to '+-...' for strip by '+' symbol
    return quadratic_form.replace('-', '+-').split("+")


def ParseCoefficient(quadratic_form: str) -> np.array:
    """
    """
    variables = GetUniqueTokens(quadratic_form)
    assert(len(variables) == 2)
    # Empty coefficient matrix to return
    c_matrix: np.array = np.array([[0, 0, 0],
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
            c_matrix[pos[0]][pos[1]] = GetInt(formatted_term)
    return c_matrix


if __name__ == '__main__':
    q_form = "-x^2 + 12 * xy - 11y^2 - 5x + 10 y + 3"
    print(ParseCoefficient(q_form))
