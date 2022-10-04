#!/bin/sh

#if pytest -m unittest ; then
#    echo "unit tests ok!"
#else
#    echo "unit tests failed!"
#    exit 1
#fi

if vulture . ; then
    echo "vulture ok!"
else
    echo "vulture failed! Will not commit."
    exit 1
fi

if isort . -c ; then
    echo "isort ok!"
else
    echo "isort failed! Will not commit."
    exit 1
fi

if black . --check ; then
    echo "black ok!"
else
    echo "black failed! Will not commit."
    exit 1
fi

if flake8 . ; then
    echo "flake8 ok!"
else
    echo "flake8 failed! Will not commit."
    exit 1
fi

if dmypy run . ; then
    echo "mypy ok!"
else
    echo "mypy failed! Will not commit."
    exit 1
fi