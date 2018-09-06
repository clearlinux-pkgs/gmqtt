#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmqtt
Version  : 0.0.22
Release  : 1
URL      : https://files.pythonhosted.org/packages/90/5d/853e2ec8a030fe3ad9b901534ea800e921700fb49a4fad2c96cce66cb071/gmqtt-0.0.22.tar.gz
Source0  : https://files.pythonhosted.org/packages/90/5d/853e2ec8a030fe3ad9b901534ea800e921700fb49a4fad2c96cce66cb071/gmqtt-0.0.22.tar.gz
Summary  : Client for MQTT protocol
Group    : Development/Tools
License  : MIT
Requires: gmqtt-python3
Requires: gmqtt-license
Requires: gmqtt-python
BuildRequires : buildreq-distutils3

%description
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
Requires: gmqtt-python3

%description python
python components for the gmqtt package.


%package python3
Summary: python3 components for the gmqtt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gmqtt package.


%prep
%setup -q -n gmqtt-0.0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536260343
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/gmqtt
cp LICENSE %{buildroot}/usr/share/doc/gmqtt/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/gmqtt/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
