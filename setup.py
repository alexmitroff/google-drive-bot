
from setuptools import setup, find_packages

setup(
   name='google-drive-bot',
   version='0.1',
   description='Simplified Google Drive bot',
   author='Aleksei Mitrofanov',
   author_email='alexmitroff@gmail.com',
   packages=find_packages(),
   install_requires=['google-api-python-client', 'google-auth-httplib2', 'google-auth-oauthlib'],
   entry_points={
       'console_scripts': [
         'send-or-update = commands.send_or_update:send_or_update',
       ]
   },
)