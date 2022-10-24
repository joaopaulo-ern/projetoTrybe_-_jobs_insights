from src.counter import count_ocurrences


def test_counter():
    javascript = count_ocurrences('src/jobs.csv', 'javascript')
    PYTHON = count_ocurrences('src/jobs.csv', 'PYTHON')
    assert javascript == 122
    assert PYTHON == 1639
    pass
