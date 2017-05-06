from distutils.core import setup, Extension

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(name             = 'RPiGPIO',
      version          = '0.2',
      author           = 'various',
      author_email     = 'willi.firulais@lycos.com',
      description      = 'enables us to use the GPIOs on a Raspberry Pi from Snap!.',
      long_description = open('README.md').read(),
      license          = 'GPL',
      keywords         = 'Snap! Raspberry Pi GPIO',
      url              = 'https://github.com/firulais/snap-RPi',
      classifiers      = classifiers,
      packages         = ['MockupRPi']
)