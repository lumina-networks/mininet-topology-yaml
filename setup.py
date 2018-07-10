import setuptools

setuptools.setup(
    name="mininet-topology-yaml",
    version="0.1.1",
    url="https://github.com/luminanetworks/mininet-topology-yaml",

    author="Lumina NetDev",
    author_email="oss-dev@luminanetworks.com",

    description="Mininet specific topology generator and parser",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['click', 'topology-yaml==0.1.1'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points='''
        [topology.plugins]
        mininet=mn_topo.cli:mininet
    ''',
)
