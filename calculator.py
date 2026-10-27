"""Simple addition calculator with a command line interface."""
import argparse
from decimal import Decimal, InvalidOperation


def add(a, b):
    return Decimal(str(a)) + Decimal(str(b))


def main():
    parser = argparse.ArgumentParser(description="PyJen027: Add two numbers")
    parser.add_argument("a", nargs="?")
    parser.add_argument("b", nargs="?")
    args = parser.parse_args()
    try:
        a = args.a if args.a is not None else input("First number: ")
        b = args.b if args.b is not None else input("Second number: ")
        result = add(a, b)
        if not result.is_finite():
            raise InvalidOperation
        print(f"{a} + {b} = {result}")
    except (InvalidOperation, ValueError):
        parser.error("Please enter valid finite numbers")


if __name__ == "__main__":
    main()
