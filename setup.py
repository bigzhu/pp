from __future__ import unicode_literals
from setuptools import setup
lib_classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]
setup(name="pp_bz",
      version='1.1.6',
      author="bigzhu",
      author_email="vermiliondun@gmail.com",
      url="https://github.com/bigzhu/pp",
      keywords='password producer',
      py_modules=["pp"],
      install_requires=[],
      description='use your key and site url create your site unique password',
      license="MIT",
      classifiers=lib_classifiers,
      entry_points={
          "console_scripts": [
              "pp = pp:main",
          ],
      },
      )
