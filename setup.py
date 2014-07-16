from setuptools import setup, find_packages

version = '1.2.7.dev0'

setup(name='collective.schedulefield',
      version=version,
      description="zope schedule field with widget",
      long_description=open("README.md").read() + "\n" +
          open("HISTORY.txt").read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='z3cform schedule field widget',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='https://github.com/collective/collective.schedulefield',
      license='GPL version 2',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.form',
          'zope.deprecation'
      ],
      extras_require=dict(test=[
            'z3c.form',
            'zope.browserpage',
            'zope.publisher',
            'zope.testing',
            'zope.traversing',
            'zc.buildout',
            'Zope2',
            ]),
      )
