#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab_server
Version  : 1.0.6
Release  : 14
URL      : https://files.pythonhosted.org/packages/05/ee/0f29b8a962a17a38f79ecac234973bccb32d215eb392f5fa5a51508e9dcc/jupyterlab_server-1.0.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/ee/0f29b8a962a17a38f79ecac234973bccb32d215eb392f5fa5a51508e9dcc/jupyterlab_server-1.0.6.tar.gz
Summary  : Launch an application built using JupyterLab
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab_server-license = %{version}-%{release}
Requires: jupyterlab_server-python = %{version}-%{release}
Requires: jupyterlab_server-python3 = %{version}-%{release}
Requires: Jinja2
Requires: json5
Requires: jsonschema
Requires: notebook
BuildRequires : Jinja2
BuildRequires : buildreq-distutils3
BuildRequires : json5
BuildRequires : jsonschema
BuildRequires : notebook

%description
# jupyterlab server
https://github.com/jupyterlab/jupyterlab_server
## Install
`pip install jupyterlab_server`

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

%description python3
python3 components for the jupyterlab_server package.


%prep
%setup -q -n jupyterlab_server-1.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567897632
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab_server
cp LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab_server/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab_server/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
