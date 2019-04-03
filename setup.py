from distutils.core import setup
setup(
	name='pyprofyler',
	version='1.0.0',
	author='Aly Shmahell',
	author_email='aly.shmahell@gmail.com',
	description='a simple memory profiler for python programs.',
	license="Copyrights © 2019 Aly shmahell.",
	packages=['pyprofyler'],
	install_requires=[
			  "psutil==5.6.1",
			  "cython==0.29.6",
			  "numpy==1.16.2"
			]
)