import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='studentrecords',
    version='0.1',
    packages=['studentrecords', 'studentrecords.managers'],
    include_package_data=True,
    license='MIT License',
    description='ИС для кафедры МО ЭВМ в ЛЭТИ',
    long_description=README,
    url='none',
    author='EvgeniyGor',
    author_email='gorodilov.box@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
