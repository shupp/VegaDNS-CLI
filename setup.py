from setuptools import setup

setup(name='vegadns_cli',
      version='0.1.1',
      description='VegaDNS CLI tool',
      # long_description=open('README.md').read(),
      url='https://github.com/shupp/VegaDNS',
      author='Bill Shupp',
      author_email='hostmaster@shupp.org',
      license='Apache 2.0',
      install_requires=[
        "click==6.4",
        "dnspython==1.12.0",
        "nose==1.3.7",
        "pep8==1.7.0",
        "requests==2.20.0",
      ],
      packages=[
        'vegadns_cli',
        'vegadns_cli.commands',
        'vegadns_client',
        'vegadns_client.store'
    ],
      scripts=['vdns'],
      zip_safe=False)
