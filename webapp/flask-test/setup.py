from setuptools import setup

setup(name='UsingSessions', version='1.0',
      description='Code example demonstrating how to manage a JSON request using Flask',
      author='Miguel Molina', author_email='info@runnable.com',
      url='http://www.runnable.com/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask',
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )