import sys

# OK = 0
# BAD_ARGS = 1
# BAD_VERB = 2
# BAD_KEY = 3

from enum import Enum, unique, auto

EXIT_SUCCESS = 1
BAD_INPUT = 2


@unique
class MetaCommandResult(Enum):

    META_COMMAND_SUCCESS = auto()
    META_COMMAND_UNRECOGNIZED_COMMAND = auto()


@unique
class PrepareResult(Enum):

    PREPARE_SUCCESS = auto()
    PREPARE_SYNTAX_ERROR = auto()
    PREPARE_UNRECOGNIZED_STATEMENT = auto()


@unique
class ExecuteResult(Enum):

    ECXCUTE_SUCCESS = auto()
    EXECUTE_TABLE_FULL = auto()


@unique
class StatementType(Enum):

    STATEMENT_INSERT = auto()
    STATEMENT_SELECT = auto()


class Statement:

    def __init__(self, statement_type=None):
        self.statement_type = statement_type


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
        exit(BAD_INPUT.value)

    return line


def do_meta_cmd(line):
    if line == '.exit':
        # return MetaCommandResult.META_COMMAND_SUCCESS
        print('exit.')
        exit(EXIT_SUCCESS)

    return MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND


def prepare_statement(line, statement):
    if 'insert' in line:
        statement.statement_type = StatementType.STATEMENT_INSERT
        return PrepareResult.PREPARE_SUCCESS
    elif 'select' in line:
        statement.statement_type = StatementType.STATEMENT_SELECT
        return PrepareResult.PREPARE_SUCCESS

    return PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT


def exec_statement(statement):
    if statement.statement_type == StatementType.STATEMENT_INSERT:
        print('This is where we would do an insert.')
        return ExecuteResult.ECXCUTE_SUCCESS
    elif statement.statement_type == StatementType.STATEMENT_SELECT:
        print("This is where we would do a select.")
        return ExecuteResult.ECXCUTE_SUCCESS
    # else:
    #     return ExecuteResult.


def main(argv):
    print('================ RodanDB ================')
    # REPL
    while True:
        print_prompt()
        line = read_input()

        if line[0] == '.':
            ans = do_meta_cmd(line)
            if ans == MetaCommandResult.META_COMMAND_SUCCESS:
                continue
            elif ans == MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND:
                print(f"Unrecognized command '{line}'")
                continue

        statement = Statement()
        prepare_res = prepare_statement(line, statement)
        if prepare_res == PrepareResult.PREPARE_SUCCESS:
            pass
        elif prepare_res == PrepareResult.PREPARE_SYNTAX_ERROR:
            print("prepare systax error")
        elif prepare_res == PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT:
            print(f"prepare unrecognized keyword error: {line}")

        exec_res = exec_statement(statement)
        if exec_res == ExecuteResult.ECXCUTE_SUCCESS:
            print('Executed.')


if __name__ == "__main__":
    sys.exit(main(sys.argv))
