from functools import lru_cache
import csv


@lru_cache
def read(path: str) -> dict:
    with open(path, encoding="utf-8", mode="r") as data:
        jobs_reader = csv.DictReader(data, delimiter=",", quotechar='"')
        return [*jobs_reader]

    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file
    Returns
    -------
    list
        List of rows as dicts
    """
