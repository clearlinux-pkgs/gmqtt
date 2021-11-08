#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmqtt
Version  : 0.5.1
Release  : 42
URL      : https://files.pythonhosted.org/packages/17/ab/a3c884fb01e67df233ee878ff54dbb0c1e5297b828d7399afb7d089c68f7/gmqtt-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/ab/a3c884fb01e67df233ee878ff54dbb0c1e5297b828d7399afb7d089c68f7/gmqtt-0.5.1.tar.gz
Summary  : Client for MQTT protocol
Group    : Development/Tools
License  : MIT
Requires: gmqtt-license = %{version}-%{release}
Requires: gmqtt-python = %{version}-%{release}
Requires: gmqtt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
### Python MQTT client implementation.
        
        ![](./static/logo.png)
        
        ### Installation 
        
        The latest stable version is available in the Python Package Index (PyPi) and can be installed using
        ```bash
        pip3 install gmqtt
        ```
        
        
        ### Usage
        #### Getting Started

%package license
Summary: license components for the gmqtt package.
Group: Default

%description license
license components for the gmqtt package.


%package python
Summary: python components for the gmqtt package.
Group: Default
Requires: gmqtt-python3 = %{version}-%{release}

%description python
python components for the gmqtt package.


%package python3
Summary: python3 components for the gmqtt package.
Group: Default
Requires: python3-core
Provides: pypi(gmqtt)

%description python3
python3 components for the gmqtt package.


%prep
%setup -q -n gmqtt-0.5.1
cd %{_builddir}/gmqtt-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636403364
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
mkdir -p %{buildroot}/usr/share/package-licenses/gmqtt
cp %{_builddir}/gmqtt-0.5.1/LICENSE %{buildroot}/usr/share/package-licenses/gmqtt/03c27e3e7b67f7256a1223d8c79042655f96cb28
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3*/site-packages/examples/__init__.py
rm -f %{buildroot}*/usr/lib/python3*/site-packages/examples/__pycache__/__init__.cpython-3*.pyc
## install_append content
rm -rf %{buildroot}/usr/lib/python3*/site-packages/tests
## install_append end

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gmqtt/03c27e3e7b67f7256a1223d8c79042655f96cb28

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
