from setuptools import setup

setup(name='BrNP',
      version='0.1',
      description='Parses news from brazillian news hubs',
      url='http://github.com/TheTonon/br_noticias_parser',
      author='Vinicius Tonon',
      author_email='viniciustonon@gmail.com',
      license='GPL',
      packages=['BrNP'],
      install_requires=[
          'lxml',
          'BeautifulSoup4',
      ],
      zip_safe=False)