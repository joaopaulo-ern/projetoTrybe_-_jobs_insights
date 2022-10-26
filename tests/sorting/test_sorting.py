from src.sorting import sort_by

from operator import itemgetter


jobs = [
    {'min_salary': 2500, 'max_salary': 3500, 'date_posted': '1995-01-02'},
    {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2000-01-02'},
    {'min_salary': 1500, 'max_salary': 2500, 'date_posted': '2005-01-02'},
    {'min_salary': 2000, 'max_salary': 3000, 'date_posted': '2010-01-02'},
]


def test_sort_by_criteria():

    sort_by(jobs, 'max_salary')
    assert jobs == sorted(jobs, key=itemgetter('max_salary'), reverse=True)

    sort_by(jobs, 'min_salary')
    assert jobs == sorted(jobs, key=itemgetter('min_salary'))

    sort_by(jobs, 'date_posted')
    assert jobs == sorted(jobs, key=itemgetter('date_posted'), reverse=True)
