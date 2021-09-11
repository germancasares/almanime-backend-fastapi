from subprocess import call, check_call
from pathlib import Path

import uvicorn


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


def lint():
    """
    Run the linter. Equivalent to:
    `poetry run pylint app -j 0`
    """
    call(
        ['pylint', 'app', '-j', '0', '--output-format=colorized']
    )


def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover -v`
    """
    check_call(
        ['python', '-u', '-m', 'unittest', 'discover', '-v']
    )


def lint_ci():
    """
    Run the linter and store the results in reports/junit/py-lint-results.xml
    """
    check_call(
        [
            'pylint', 'app',
            '-j', '0',
            '--disable=C',
            '--output-format=pylint_junit.JUnitReporter:reports/junit/py-lint-results.xml,colorized'
        ]
    )


def test_ci():
    """
    Run all the tests and store the results in reports/junit/py-test-results.xml
    """
    Path("./reports/junit").mkdir(parents=True, exist_ok=True)
    check_call(
        ['python', '-u', '-m', 'xmlrunner', 'discover',
            '-v', '--output-file', './reports/junit/py-test-results.xml']
    )


def audit_ci():
    """
    Run all unittests. Equivalent to:
    `poetry run safety check --full-report`
    """
    check_call(
        ['safety', 'check', '--full-report']
    )
