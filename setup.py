from setuptools import setup, find_packages

requires = [
    'requests>=2.18.4',
    'pync>=1.6.1',
]
setup(name='instagram-stalker',
      version='0.2.0',
      description="Observes given instagram account and notify when he makes his account public.",
      url='http://github.com/pkacprzak/instagram-stalker',
      author='Pawel Kacprzak',
      author_email='pawel.kacprzak.89@gmail.com',
      license='Public domain',
      packages=find_packages(exclude=['tests']),
      install_requires=requires,entry_points={
        'console_scripts': ['instagram-stalker=instagram_stalker.app:main'],
      },
      keywords=['instagram', 'scraper', 'stalker', 'observer', 'photos' ],
      zip_safe=False)


