import sys

# OK = 0
# BAD_ARGS = 1
# BAD_VERB = 2
# BAD_KEY = 3

EXIT_SUCCESS = 0
BAD_INPUT = -1

# def usage():
#     print("Usage:", file=sys.stderr)
#     print("\tpython -m rodan.tool DBNAME get KEY", file=sys.stderr)
#     print("\tpython -m rodan.tool DBNAME set KEY VALUE", file=sys.stderr)
#     print("\tpython -m rodan.tool DBNAME delete KEY", file=sys.stderr)


def print_prompt():
    print('db > ', end='')


def read_input():
    line = input()
    print(f"echo => {line}, len: {len(line)}")

    if len(line) <= 0:
        print("Error reading input")
        exit(BAD_INPUT)

    return line


def main(argv):

    print('================ RodanDB ================')
    # REPL
    while True:
        print_prompt()
        line = read_input()

        if line == '.exit':
            exit(EXIT_SUCCESS)
        else:
            print(f"Unrecognized command {line}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
