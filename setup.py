import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='studentrecords',
    version='0.1',
    packages=['studentrecords'],
    include_package_data=True,
    license='MIT License',
    description='ИС для кафедры МО ЭВМ в ЛЭТИ',
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
    ], install_requires=['django']
)
