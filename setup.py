from setuptools import setup

setup(
    name='py-store',
    version='0.0.6',
    description='Webscraping for stores',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Naegin',
    author_email='discord.naegin@gmail.com',
    url='https://github.com/naegin/py-store',
    download_url='https://github.com/naegin/py-store/archive/master.zip',
    license='MIT',
    packages=['store'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)
