from setuptools import setup, find_packages

setup(
        name='LearningPython',
        version='0.0.1',
        url='www.github.com/2nitinagarwal/LearningPython',
        license='BSD',
        author='Nitin Agarwal',
        packages=find_packages(),
        install_requires=['PyQt5',
                          'pandas',
                          'sqlalchemy',
                          'nltk',
                          'numpy',
                          'jupyter',
                          'python-twitter'],
        entry_point={},
        extras_require={'dev': ['flake8',]},
        )
