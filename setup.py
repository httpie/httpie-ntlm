from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

import httpie_ntlm


setup(
    name='httpie-ntlm',
    description=httpie_ntlm.__doc__.strip(),
    long_description=open('README.rst').read().strip(),
    version=httpie_ntlm.__version__,
    author=httpie_ntlm.__author__,
    author_email='jakub@roztocil.name',
    license=httpie_ntlm.__licence__,
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
