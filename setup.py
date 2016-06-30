# -*- coding: utf-8 -*-
__revision__ = "$Id: $"

import sys
import os

from setuptools import setup, find_packages


#The metainfo files must contains
# version, release, project, name, namespace, pkg_name,
# description, long_description,
# authors, authors_email, url and license
# * version is 1.0.0 and release 1.0
# * project must be in [openalea, vplants, alinea]
# * name is the full name (e.g., VPlants.autowig) whereas pkg_name is only 'autowig'

# name will determine the name of the egg, as well as the name of
# the pakage directory under Python/lib/site-packages). It is also
# the one to use in setup script of other packages to declare a dependency to this package)
# (The version number is used by deploy to detect UPDATES)


# Packages list, namespace and root directory of packages

pkg_root_dir = 'src'
pkgs = [ pkg for pkg in find_packages(pkg_root_dir)]
top_pkgs = [pkg for pkg in pkgs if  len(pkg.split('.')) < 2]
packages = pkgs
package_dir = dict( [('',pkg_root_dir)] + [(namespace + "." + pkg, pkg_root_dir + "/" + pkg) for pkg in top_pkgs] )

# Define global variables
has_scons = False
if has_scons:
    build_prefix = "build-scons"
    scons_scripts=['SConstruct']
    lib_dirs = {'lib' : build_prefix+'/lib' }
    inc_dirs = { 'include' : build_prefix+'/include' }
    bin_dirs = { 'bin' : build_prefix+'/bin' }
else:
    build_prefix = None
    scons_scripts=None
    lib_dirs = None
    inc_dirs = None
    bin_dirs = None

# List of top level wralea packages (directories with __wralea__.py)
#wralea_entry_points = ['%s = %s'%(pkg,namespace + '.' + pkg) for pkg in top_pkgs]

# dependencies to other eggs
setup_requires = ['openalea.deploy']
if("win32" in sys.platform):
    install_requires = []
else:
    install_requires = []

# web sites where to find eggs
dependency_links = ['http://openalea.gforge.inria.fr/pi']
setup(
    name="AutoWIG",
    version="0.1.0",
    description="AUTOmatic Wrapper and Interface Generator package",
    long_description="",
    author="P. Fernique, C. Pradal",
    author_email="pierre.fernique@inria.fr, christophe.pradal@cirad.fr",
    url="autowig.readthedocs.org",
    license="CeCILL-C",
    keywords = '',

    # package installation
    packages= packages,
    package_dir= package_dir,

    # Namespace packages creation by deploy
    #namespace_packages = [namespace],
    #create_namespaces = False,
    zip_safe= False,

    # Dependencies
    setup_requires = setup_requires,
    install_requires = install_requires,
    dependency_links = dependency_links,

    # Eventually include data in your package
    # (flowing is to include all versioned files other than .py)
    include_package_data = True,
    # (you can provide an exclusion dictionary named exclude_package_data to remove parasites).
    # alternatively to global inclusion, list the file to include
    #package_data = {'' : ['*.pyd', '*.so'],},

    # postinstall_scripts = ['',],

    # Declare scripts and wralea as entry_points (extensions) of your package
    entry_points = {
        'autowig.parser': ['libclang = autowig.libclang_parser:libclang_parser'],
        'autowig.controller': ['default = autowig.default_controller:default_controller'],
        'autowig.generator': ['boost_python = autowig.boost_python_generator:boost_python_generator',
            'boost_python_pattern = autowig.boost_python_generator:boost_python_pattern_generator',
            'boost_python_internal = autowig.boost_python_generator:boost_python_internal_generator',
            'boost_python_closure = autowig.boost_python_generator:boost_python_closure_generator'],
        'autowig.visitor': ['boost_python = autowig.boost_python_generator:boost_python_visitor',
            'all = autowig.asg:all_visitor',
            'free = autowig.asg:free_visitor',
            'public = autowig.asg:public_visitor',
            'protected = autowig.asg:protected_visitor',
            'private = autowig.asg:private_visitor'],
        'autowig.feedback' : ['gcc-5 = autowig.gcc_feedback:gcc_5_feedback'],
        'autowig.boost_python_call_policy': ['default = autowig.boost_python_generator:boost_python_default_call_policy'],
        'autowig.boost_python_export': ['custom = autowig.boost_python_generator:BoostPythonExportFileProxy',
            'basic = autowig.boost_python_generator:BoostPythonExportBasicFileProxy',
            'mapping = autowig.boost_python_generator:BoostPythonExportMappingFileProxy'],
        'autowig.boost_python_module': ['default = autowig.boost_python_generator:BoostPythonModuleFileProxy'],
        'autowig.boost_python_decorator': ['default = autowig.boost_python_generator:BoostPythonDecoratorDefaultFileProxy'],
        'autowig.node_rename': ['PEP8 = autowig.node_rename:pep8_node_rename'],
        'autowig.documenter': ['doxygen2sphinx = autowig.doxygen2sphinx:doxygen2sphinx_documenter'],
        'autowig.node_path' : ['scope = autowig.node_path:scope_node_path',
            'hash = autowig.node_path:hash_node_path'],
        'console_scripts': [],
        # 'gui_scripts': [
        #      'fake_gui = openalea.fakepackage.amodule:gui_script',],
        #	'wralea': wralea_entry_points
        },
    )


