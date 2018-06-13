%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define packagename ukaz

Name:          tcl-ukaz
Summary:       Graph widget in pure Tcl/Tk
Version:       2.0a3
Release:       0
License:       MIT
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://github.com/auriocus/ukaz
BuildArch:     noarch
BuildRequires: tcl >= 8.6
Requires:      tcl >= 8.6
Requires:      tk >= 8.6
Requires:      tcllib
BuildRoot:     %{buildroot}

%description
A graph widget written in pure Tcl/Tk.

This is a package which provides a widget to plot data in x-y format for
scientific applications.

%prep
%setup -q -n ukaz-%{version}

%build

%install
dir=%buildroot%tcl_noarchdir/%packagename%version
mkdir -p $dir
cp *.tcl $dir

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README.md LICENSE demo
%tcl_noarchdir/%packagename%version

