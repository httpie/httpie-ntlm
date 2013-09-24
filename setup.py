from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='httpie-ntlm',
    description='NTLM auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='1.0.2',
    author='Jakub Roztocil',
    author_email='jakub@roztocil.name',
    license='BSD',
    url='https://github.com/jkbr/httpie-ntlm',
    download_url='https://github.com/jkbr/httpie-ntlm',
    py_modules=['httpie_ntlm'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_ntlm = httpie_ntlm:NTLMAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'requests_ntlm'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
