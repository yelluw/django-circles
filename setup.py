from setuptools import setup, find_packages

setup(
    name='django-circles',
    version='0.1.0',
    description='A Django app to create circles of collaborators.',
    url='https://github.com/yelluw/django-circles',
    author='Pablo Rivera',
    author_email='pryelluw@gmail.com',
    classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 3.0',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django collaborators users circles',
    packages=find_packages(),
    python_requires='>=3.5',
)