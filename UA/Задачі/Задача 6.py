from posixpath import split


def snake_case(s, sep):
    return "_".join(s.split(sep))