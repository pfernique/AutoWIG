.. ................................................................................ ..
..                                                                                  ..
..  AutoWIG: Automatic Wrapper and Interface Generator                              ..
..                                                                                  ..
..  Homepage: http://autowig.readthedocs.io                                         ..
..                                                                                  ..
..  Copyright (c) 2016 Pierre Fernique                                              ..
..                                                                                  ..
..  This software is distributed under the CeCILL license. You should have        ..
..  received a copy of the legalcode along with this work. If not, see              ..
..  <http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html>.                  ..
..                                                                                  ..
..  File authors: Pierre Fernique <pfernique@gmail.com> (9)                         ..
..                                                                                  ..
.. ................................................................................ ..

.. _install-source:

Installation from source code
=============================

.. note::

    When installing **AutoWIG** from source code, it is highly recommanded to first install **PyClangLite** from source code (refers to its `installation guide <http://pyclanglite.readthedocs.io/en/latest/source.html>`_).
    
In order to install **AutoWIG** from source code we recommand to:

* Download the source code available on *GitHub* (see `Git <https://git-scm.com/>`_ and `GitHub <https://github.com/>`_ websites for more information).

  .. code-block:: bash
  
      git clone https://github.com/StatisKit/AutoWIG.git
      cd AutoWIG
     
* Use the conda recipes present on this repository (see `conda <http://conda.pydata.org/docs/>`_ website for more information).
 
  .. literalinclude:: ../../conda/build.sh
     :lines: 4-

  .. note::
 
      Following this procedure do not install *Python* packages in develop mode.
      
  .. warning::

      This installation has only been tested on **Ubuntu**.

.. warning::

    When installing **AutoWIG** from source code, it is highly recommanded to install **Boost** libraries from source code (refers to its `installation guide <http://www.boost.org/doc/libs/release/more/getting_started/index.html>`_).
