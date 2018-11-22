#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmqtt
Version  : 0.2.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/c8/93/f47ceacea015aefbb7821728bc5ec3f280e8260b6296fb1440b52f5d06fe/gmqtt-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/93/f47ceacea015aefbb7821728bc5ec3f280e8260b6296fb1440b52f5d06fe/gmqtt-0.2.0.tar.gz
Summary  : Client for MQTT protocol
Group    : Development/Tools
License  : MIT
Requires: gmqtt-license = %{version}-%{release}
Requires: gmqtt-python = %{version}-%{release}
Requires: gmqtt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
### Python MQTT client implementation.
        
        
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

%description python3
python3 components for the gmqtt package.


%prep
%setup -q -n gmqtt-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542910071
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gmqtt
cp LICENSE %{buildroot}/usr/share/package-licenses/gmqtt/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gmqtt/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.7/site-packages/tests/__init__.py
%exclude /usr/lib/python3.7/site-packages/tests/__pycache__/__init__.cpython-37.pyc
/usr/lib/python3*/*
