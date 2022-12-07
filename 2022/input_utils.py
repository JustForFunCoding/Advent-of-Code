def get_text(filename: str) -> str:
    return open(filename).read()


def get_unstripped_lines(filename: str) -> list[str]:
    return open(filename).readlines()


def get_lines(filename: str) -> list[str]:
    return list(map(str.strip, get_unstripped_lines(filename)))


def get_line_groups(filename: str) -> list[list[str]]:
    return list(map(str.split, get_text(filename).strip().split('\n\n')))


def get_numbers(filename: str) -> list[int]:
    return list(map(int, get_lines(filename)))


def get_number_groups(filename: str) -> list[list[int]]:
    return list(map(lambda s: list(map(int, s.split())),
                    get_text(filename).strip().split('\n\n')))
