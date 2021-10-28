#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab_server
Version  : 2.8.2
Release  : 56
URL      : https://files.pythonhosted.org/packages/79/41/552120becdd267b505f6aafc522c0d90bb051d780cd1b1e7429286b01418/jupyterlab_server-2.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/79/41/552120becdd267b505f6aafc522c0d90bb051d780cd1b1e7429286b01418/jupyterlab_server-2.8.2.tar.gz
Summary  : A set of server components for JupyterLab and JupyterLab like applications .
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab_server-license = %{version}-%{release}
Requires: jupyterlab_server-python = %{version}-%{release}
Requires: jupyterlab_server-python3 = %{version}-%{release}
Requires: Babel
Requires: Jinja2
Requires: entrypoints
Requires: json5
Requires: jsonschema
Requires: packaging
Requires: requests
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : buildreq-distutils3
BuildRequires : entrypoints
BuildRequires : json5
BuildRequires : jsonschema
BuildRequires : jupyter_server
BuildRequires : packaging
BuildRequires : requests

%description
# jupyterlab server
[![Coverage](https://codecov.io/gh/jupyterlab/jupyterlab_server/branch/master/graph/badge.svg)](https://codecov.io/gh/jupyterlab/jupyterlab_server)
[![Build Status](https://github.com/jupyterlab/jupyterlab_server/workflows/Tests/badge.svg?branch=master)](https://github.com/jupyterlab/jupyterlab_server/actions?query=branch%3Amaster+workflow%3A%22Tests%22)
[![Documentation Status](https://readthedocs.org/projects/jupyterlab_server/badge/?version=stable)](http://jupyterlab_server.readthedocs.io/en/stable/)

%package license
Summary: license components for the jupyterlab_server package.
Group: Default

%description license
license components for the jupyterlab_server package.


%package python
Summary: python components for the jupyterlab_server package.
Group: Default
Requires: jupyterlab_server-python3 = %{version}-%{release}

%description python
python components for the jupyterlab_server package.


%package python3
Summary: python3 components for the jupyterlab_server package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_server)
Requires: pypi(babel)
Requires: pypi(entrypoints)
Requires: pypi(jinja2)
Requires: pypi(json5)
Requires: pypi(jsonschema)
Requires: pypi(jupyter_server)
Requires: pypi(packaging)
Requires: pypi(requests)

%description python3
python3 components for the jupyterlab_server package.


%prep
%setup -q -n jupyterlab_server-2.8.2
cd %{_builddir}/jupyterlab_server-2.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632753508
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab_server
cp %{_builddir}/jupyterlab_server-2.8.2/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab_server/5c2668cefc1e214f589e49594127f9f79574de44
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab_server/5c2668cefc1e214f589e49594127f9f79574de44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
