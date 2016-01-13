from distutils.core import setup

description = 'A python library for interacting with the Apple Push Notification Service'
setup(
      author='Simon Whitaker',
      author_email='simon@goosoftware.co.uk',
      description=description,
      download_url='http://github.com/simonwhitaker/PyAPNs',
      license='unlicense.org',
      name='apns',
      py_modules=['apns'],
      scripts=['apns-send'],
      url='http://www.goosoftware.co.uk/',
      version='1.1.2',
)
