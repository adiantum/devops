from setuptools import setup

setup(
    name='devops',
    version='2.0',
    description='Library for creating and manipulating virtual environments',
    author='Mirantis, Inc.',
    author_email='product@mirantis.com',
    packages=['devops', 'devops.driver', 'devops.helpers', 'devops.tests',
              'devops.driver.libvirt'],
    package_dir={'': 'src'},
    scripts=['src/dos.py'],
    install_requires=['xmlbuilder', "ipaddr", "paramiko", "django==1.4.3", "psycopg2"]
)
