from src.jobs import read


def get_unique_job_types(path: str) -> set:
    data = read(path)
    conjunto = set()

    for linha in data:
        if linha['job_type'] != '':
            conjunto.add(linha['job_type'])

    return conjunto

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]

    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """


def get_unique_industries(path):
    data = read(path)
    conjunto = set()

    for linha in data:
        if linha['industry'] != '':
            conjunto.add(linha['industry'])

    return conjunto

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    data = read(path)
    conjunto = set()

    for linha in data:
        if linha['max_salary'].isnumeric():
            conjunto.add(int(linha['max_salary']))

    return max(conjunto)

    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    pass


def get_min_salary(path):
    data = read(path)
    conjunto = set()

    for linha in data:
        if linha['min_salary'].isnumeric():
            conjunto.add(int(linha['min_salary']))

    return min(conjunto)

    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    try:
        minimo = job["min_salary"]
        maximo = job["max_salary"]
    except KeyError:
        raise ValueError("Erro nas categorias informadas")
    conjuto_tipos = set([type(minimo), type(maximo), type(salary)])
    if type(salary) != int or len(conjuto_tipos) != 1:
        raise ValueError("Algum elemento(min, max ou salary) não é inteiro")
    elif minimo > maximo:
        raise ValueError("Valor minimo maior que o máximo")
    else:
        return minimo <= salary <= maximo

    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    salarios = []
    for linha in jobs:
        try:
            if (matches_salary_range(linha, salary)):
                salarios.append(linha)
        except ValueError:
            pass
    return salarios
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
