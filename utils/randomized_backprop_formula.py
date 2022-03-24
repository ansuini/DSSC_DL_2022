import random
import hashlib
from pprint import pprint

class Operator():
    def __init__(self):
        raise NotImplementedError("this is an abstract class")
    
    def __str__(self):
        raise NotImplementedError("this is an abstract class")


class UnaryOperator():
    def __init__(self, symbol, child, when_print="before", parentheses=False):
        self.symbol = symbol
        self.when_print = when_print
        self.children = [child]
        self.parentheses = parentheses

    def print(self):
        return 

    def __str__(self):
        print_string = ""
        if self.when_print == "before":
            print_string += str(self.symbol)

        if self.parentheses:
            print_string += "("
        print_string += self.children[0].__str__()
        if self.parentheses:
            print_string += ")"

        if self.when_print == "after":
            print_string += str(self.symbol)

        return print_string

class BinaryOperator():
    def __init__(self, symbol:Operator, children):
        self.symbol = symbol
        assert len(children) == 2, f"Needs 2 children, found {len(children)}"
        self.children = children
    
    def __str__(self):
        print_string = "(" + self.children[0].__str__() + " "
        print_string += str(self.symbol) + " "
        print_string += self.children[1].__str__() + ")"
        return print_string



if __name__ == "__main__":
    name = input("Input your name, then press ENTER: ").encode("UTF-8")
    seed = int(hashlib.md5(name).hexdigest(), 16)
    random.seed(seed)

    BINARY_OPERATORS = ["+", "-", "*", "/"]
    UNARY_OPERATORS = {
        "^2": {"when_print": "after"},
        "^3": {"when_print": "after"},
        "log": {},
        "exp": {},
        "cos": {},
        "sin": {},
        "tan": {},
        "arctan": {},
        "1/": {},
        "√": {},
        "ReLU": {},
        "LeakyReLU": {},
    }

    def sample_nonzero():
        return random.choice([-1,1])*random.randint(1,5)

    roots_dict = {"x1": sample_nonzero(), "x2": sample_nonzero(), "x3": sample_nonzero(), "x4": sample_nonzero(), "x5": sample_nonzero()}
    roots = list(roots_dict.keys())

    bin1 = BinaryOperator(random.choice(BINARY_OPERATORS), children=roots[:2])
    bin2 = BinaryOperator(random.choice(BINARY_OPERATORS), children=roots[2:4])
    
    una1_symbol, una1_args = random.choice(list(UNARY_OPERATORS.items()))
    una1 = UnaryOperator(una1_symbol, child=bin1, **una1_args)
    una2_symbol, una2_args = random.choice(list(UNARY_OPERATORS.items()))
    una2 = UnaryOperator(una2_symbol, child=bin2, **una2_args)

    bin3 = BinaryOperator(random.choice(BINARY_OPERATORS), children=[una1, una2])
    bin4 = BinaryOperator(random.choice(BINARY_OPERATORS), children=[bin3, roots[-1]])

    una3_symbol, una3_args = random.choice(list(UNARY_OPERATORS.items()))
    una3 = UnaryOperator(una3_symbol, child=bin4, **una3_args)

    print("\n")
    print("f(X) = ", una3)

    print("\nYour values")
    pprint(roots_dict)

    print("\nCalculate ∇f(X) [NB: if division by 0, change the value(s) of X responsible for that]")



    

