from distutils.core import setup
setup(
  name = 'pygbx',
  packages = ['pygbx'],
  version = '0.3',
  license='GPL3',
  description = 'A Python library to parse GBX files',
  author = 'Adam Bieńkowski',              
  author_email = 'donadigos159@gmail.com',
  url = 'https://github.com/donadigo/pygbx',
  download_url = 'https://github.com/donadigo/pygbx/archive/0.3.zip',
  keywords = ['GBX', 'parser', 'TrackMania'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  package_dir={'pygbx': 'pygbx'},
  include_package_data=True,
  package_data={'pygbx': ['lzo/libs/lzo1x.*']},
  data_files=["pygbx/lzo/libs/lzo1x_32.dll", "pygbx/lzo/libs/lzo1x_64.dll", "pygbx/lzo/libs/lzo1x_32.so", "pygbx/lzo/libs/lzo1x_64.so"],
)
