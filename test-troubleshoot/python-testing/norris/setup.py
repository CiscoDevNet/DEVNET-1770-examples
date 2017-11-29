from setuptools import setup
setup(name='norris',
      version='1.0',
      install_requires=[
          'requests',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
