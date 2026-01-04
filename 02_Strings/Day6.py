"""
Given a string s of '(',')' and lowercase English characters.
Your task is to remove the minimum number of parentheses
('(' or ')', in any positions) so that the resulting parentheses
string is valid and return any valid string.

IDENTIFY UNMATCHED ): Scan from left to right, keeping track of open parentheses. 
If you see a ) without a preceding (, it's extra and must be removed.

IDENTIFY UNMATCHED (: After the first pass, any ( that never found a ) are also extra and must go.

RECONSTRUCT: Build the final string from the original, omitting the parentheses marked for removal. 
"""

# recursive function to find all valid strings
def findValid(str, index, open, close, 
    pair, cur, res):

    # base case, if end of string is reached
    if index == len(str):

        # check if all open and closed invalid
        # parenthesis are removed and no pair is left
        if open == 0 and close == 0 and pair == 0:

            # if so, store the string
            res.add(cur)
        return

    # if the current character is not a parenthesis
    if str[index] != '(' and str[index] != ')':

        # add the character to the current string
        findValid(str, index + 1, open, close, 
            pair, cur + str[index], res)
    else:

        # if the current character is an open bracket
        if str[index] == '(':

            # reduce open count by 1, 
            # and skip current character
            if open > 0:
                findValid(str, index + 1, open - 1, 
                        close, pair, cur, res)

            # add the current character to the string
            findValid(str, index + 1, open, close, 
                    pair + 1, cur + str[index], res)

        # else if the current character is a closed bracket
        else:

            # skip current character and
            #  reduce closed count by 1
            if close > 0:
                findValid(str, index + 1, open, 
                        close - 1, pair, cur, res)

            # if there is an open pair, reduce
            # it and add the current character
            if pair > 0:
                findValid(str, index + 1, open, close, 
                    pair - 1, cur + str[index], res)


def validParenthesis(str):

    # to store the unique valid strings
    result = set()

    # to store count of invalid
    # open and closed paraenthesis
    open = 0
    close = 0

    # count the number of invalid 
    # open and closed parenthesis
    for c in str:

        # if open bracket, increase
        # open invalid count by 1
        if c == '(':
            open += 1

        # if closed bracket,
        if c == ')':

            # decrement invalid open
            # count by 1 if open is not 0
            if open != 0:
                open -= 1
            
            # else increment invalid closed
            # bracket count by 1
            else:
                close += 1

    # recursive function to find all valid strings
    findValid(str, 0, open, close, 0, "", result)

    # store the unique strings in an array
    return list(result)


if __name__ == "__main__":
    str = "(v)())()"
    print(validParenthesis(str))