#! /bin/bash
rm dist/*
python setup.py bdist_wheel --universal
twine upload dist/*

sudo pip install pp_bz --upgrade
