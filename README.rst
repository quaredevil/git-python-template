.. |RepositoryOwner| replace:: 99Taxis
.. |RepositoryName| replace:: systems-engineering-git-python-template

===============
{PROJECT NAME}
===============

.. Shields (https://shields.io/)

|license| |versions| |test-status| |docs| |metacov|

.. |license| image:: https://img.shields.io/github/license/99Taxis/systems-engineering-git-python-template.svg
    :target: https://github.com/99Taxis/systems-engineering-git-python-template/blob/master/LICENSE
    :alt: License

.. |test-status| image:: https://github.com/nedbat/coveragepy/actions/workflows/testsuite.yml/badge.svg?branch=master&event=push
    :target: https://github.com/nedbat/coveragepy/actions/workflows/testsuite.yml
    :alt: Test suite status

.. |versions| image:: https://img.shields.io/pypi/pyversions/coverage.svg?logo=python&logoColor=FBE072
    :target: https://pypi.org/project/coverage/
    :alt: Python versions supported

.. |docs| image:: https://readthedocs.org/projects/coverage/badge/?version=latest&style=flat
    :target: https://coverage.readthedocs.io/
    :alt: Documentation

.. |metacov| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/8c6980f77988a327348f9b02bbaf67f5/raw/metacov.json
    :target: https://nedbat.github.io/coverage-reports/latest.html
    :alt: Coverage reports


.. |99applogo| image:: https://avatars.githubusercontent.com/u/4680924?s=400&v=4
   :alt: 99app
   :target: https://github.com/99Taxis

.. list-table::
   :widths: 600 10

   * - |99applogo|
     - Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et eros imperdiet, ullamcorper sapien id, convallis diam. Aliquam pellentesque sem a sem lacinia, eu aliquam ex dignissim. Quisque id justo eu eros dictum tristique at vitae elit. Curabitur quis leo neque. In auctor, urna viverra posuere iaculis, metus nunc aliquet erat, eu dictum neque ligula sed sapien. Vivamus ac bibendum magna.
       `Learn more. <https://#readme>`_
       

Project Setup
=============


Python_
--------------
Start the installation of Python with the command::

    sudo apt update
    sudo apt install software-properties-common
    sudo apt install python3.8


Allow the process to complete and verify the Python version was installed sucessfully::

    python --version


Poetry_
----------------
Get/install Poetry::
       
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
    
Then we need to enter the project directory and execute some commands::
    
    poetry shell

Install dependences::
    
    poetry install

If there is a problem installing the dependencies::
    
    poetry cache clear . --all
    rm poetry.lock
    poetry install
    
.. Links
.. _Python: https://www.python.org/downloads/
.. _Poetry: https://github.com/sdispater/poetry




Configuration
=============

.. list-table:: Environments
   :widths: 15 10 10
   :header-rows: 1

   * - Name
     - Default Value
     - Description
   * - GRPC_VERBOSITY
     - debug
     - Show information over transactions



Use
=============

Unit Testing
------------
``pytest`` is a unit testing platform and the package of choice when it comes to the majority of the Python ecosystem::
    
    pytest

Package Testing
---------------
``tox`` is a powerful Python testing automation package. It automates the setup and execution of the testing steps above. You can use it to test across multiple Python versions.::
    
    tox

Project Styling
---------------
``flake8`` is a fantastic package and tool that will make sure that your code is in tip-top shape.::

    flake8

Activity Diagram
=================

.. |ActivityDiagramImage| image:: https://avatars.githubusercontent.com/u/4680924?s=200&v=4
   :alt: Activity Diagram

|ActivityDiagramImage|


Deploy Diagram
==============

.. |DeployDiagramImage| image:: https://avatars.githubusercontent.com/u/4680924?s=200&v=4
   :alt: Activity Diagram

|DeployDiagramImage|

CI/CD Diagram
==============

.. |CICDDiagramImage| image:: https://avatars.githubusercontent.com/u/4680924?s=200&v=4
   :alt: Activity Diagram

|CICDDiagramImage|


Project structure
=================

Files related to structure is in the ``/ (root)`` directory.

Default parts are::

    / ("root")
    ├── .github                         - github (e.g. ci, images) stuff.
    ├── doc                             - documentation related stuff.
    ├── newsfragments                   - changelogs related stuff.    
    ├── app                             - application stuff.
    ├── .gitignore                      - parameters/directories to be ignored by git sync.
    ├── pre-commit-config.yaml          - parameters to check after commit.
    ├── LICENSE                         - use license file.
    ├── Makefile                        - 
    ├── pyproject.toml                  - 
    ├── README.md                       - development and design information.
    ├── readthedocs.yml                 - 
    ├── Makefile                        - 
    └── setup.cfg                       -


Files related to application is in the ``app`` directory.


Application parts are::

    app
    ├── grcp                            - gRPC-generated related stuff.
    ├── interceptors                    - gRPC-interceptors related stuff.
    ├── core                            - application configuration, startup events, logging, helpers, resources for all.
    ├── .devops                         - devops related stuff.
    │   └── environments                - environments stuff.
    │   │   ├── env.env                 - template for use in environment variables
    │   ├── containers                  - container/docker/kubernetes related stuff.
    │   │   ├── .dockerignore           - parameters/directories to be ignored by docker build.
    │   │   └── Dockerfile              - converting application to container.
    ├── .tls                            - digital certificate stuff.
    │   └── README.md                   - guide for generating the digital certificate.
    ├── models                          - pydantic models for this application (domains).
    ├── services                        - logic that is not just crud related.
    ├── tests                           - tests stuff.
    ├── server.py                       - web framework application creation and configuration.
    └── README.md                       - development and design information.



List of Covered Tools
=====================

Environment
----------------

* poetry_ for environments isolated


Project Styling
----------------

* flake8_ for source code checking
    * flake8-docstrings_
    * darglint_
* isort_
    * seed-isort-config_
* black_
* pre-commit_


Unit Testing 
----------------

* pytest_ for unit testing
    * pytest-cov_ 
    * pytest-mock_
    * xdoctest_   
* coverage_     
* tox_ for testing on multiple Python versions


Continuous Integration
----------------

* `GitHub Actions`_


Documentation
----------------

* sphinx_ for documentation
* readthedocs_
* sphinx_rtd_theme_


Release
----------------

* towncrier_ for changelogs
* `poetry publish`_


Documentation
----------------

* documentation_


.. Links
.. _poetry: https://github.com/sdispater/poetry
.. _flake8: https://github.com/PyCQA/flake8
.. _flake8-docstrings: https://github.com/PyCQA/flake8-docstrings
.. _darglint: https://github.com/terrencepreilly/darglint
.. _isort: https://github.com/timothycrosley/isort
.. _seed-isort-config: https://github.com/asottile/seed-isort-config
.. _black: https://github.com/psf/black
.. _pre-commit: https://github.com/pre-commit/pre-commit
.. _pytest: https://github.com/pytest-dev/pytest
.. _pytest-cov: https://github.com/pytest-dev/pytest-cov
.. _pytest-mock: https://github.com/pytest-dev/pytest-mock
.. _xdoctest: https://github.com/Erotemic/xdoctest
.. _coverage: https://github.com/nedbat/coveragepy
.. _tox: https://github.com/tox-dev/tox
.. _`GitHub Actions`: https://docs.github.com/en/actions
.. _sphinx: https://github.com/sphinx-doc/sphinx
.. _readthedocs: https://github.com/readthedocs/readthedocs.org
.. _sphinx_rtd_theme: https://github.com/readthedocs/sphinx_rtd_theme
.. _towncrier: https://github.com/hawkowl/towncrier
.. _`poetry publish`: https://poetry.eustace.io/docs/cli/#publish
.. _documentation: https://#

Issues
======

Please report any bugs or requests that you have using the GitHub issue tracker!


Authors
=======

* `Emanuel Barbosa Soares`_

.. _`Emanuel Barbosa Soares`: https://github.com/quaredevil/




    




