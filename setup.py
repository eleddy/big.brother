from setuptools import setup, find_packages
import os

version = '.1'

setup(name='big.brother',
      version=version,
      description="Keeps track of who has viewed a particular document",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='eleddy',
      author_email='me@eleddy.com',
      url='https://github.com/eleddy/big.brother',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['big'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
