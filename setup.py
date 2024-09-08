from setuptools import setup, find_packages

setup(
    name='luhns_validation',
    version='0.1',
    packages=find_packages(),
    description='A package to validate credit card numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bradley Ngan',
    author_email='bradley.ngan@gmail.com',
    url='https://github.com/BNganB/luhns',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3'
)
