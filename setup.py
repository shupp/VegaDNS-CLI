from setuptools import setup

setup(name='vegadns_cli',
      version='0.2.0',
      description='VegaDNS CLI tool',
      # long_description=open('README.md').read(),
      url='https://github.com/shupp/VegaDNS',
      author='Bill Shupp',
      author_email='hostmaster@shupp.org',
      license='Apache 2.0',
      install_requires=[
        "certifi==2022.12.7",
        "chardet==3.0.4",
        "Click==7.0",
        "dnspython==1.16.0",
        "future==0.17.1",
        "idna==2.8",
        "nose==1.3.7",
        "pycodestyle==2.5.0",
        "requests==2.22.0",
        "urllib3==1.25.8"
      ],
      packages=[
        'vegadns_cli',
        'vegadns_cli.commands',
        'vegadns_client',
        'vegadns_client.store'
    ],
      scripts=['vdns'],
      zip_safe=False)
