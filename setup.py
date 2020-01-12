from setuptools import find_packages, setup

setup(
        name='itu.algs4',
        version='0.2.1.7',
        description='Python 3 port of the Java code in "Algorithms, 4th Edition" by Sedgewick and Wayne',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        # author='',
        # author_email='',
        url='https://github.com/itu-algorithms/itu.algs4/',
        license='GNU General Public License v3 (GPLv3)',
        packages=['itu.algs4'],
        include_package_data=True,
        extras_require={
            'audio': ['numpy'],
            'visual': ['pygame'],
            'dev': ['flake8', 'isort', 'pytest', 'pytest-cov', 'coveralls', 'mypy'],
            },
        zip_safe=False,
        platforms='any',
        classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: OS Independent',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Utilities',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ]
        )
