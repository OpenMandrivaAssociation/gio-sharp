Name:           gio-sharp
Version:        2.22.3
Release:        %mkrel 0.3
License:        GPLv2 and MIT
Group:          Development/Other
Summary:        .NET/C# Bindings for GIO
Url:            https://github.com/mono/gio-sharp
Source:         https://github.com/downloads/mono/%name/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
BuildRequires:  glib2-devel >= 2.22
BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2-devel
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
Requires: glib2 > 2.22
#gw strictly speaking, it needs libgio:
Requires: gvfs
%define _requires_exceptions lib.*gio\\|lib.*glib

%description
C#/CLI bindings for GIO

%package devel
Group:          Development/Other
Summary:        .NET/C# Bindings for GIO
Requires:       %{name} = %{version}

%description devel
Files for developing programs that use gio-sharp

%prep
%setup -q

%build
%configure2_5x --libdir=%_prefix/lib
make

%install
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
#ChangeLog 
%dir %_prefix/lib/gio-sharp
%_prefix/lib/gio-sharp/gio-sharp.dll*

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/gio-sharp-2.0.pc
%dir %_prefix/share/gapi-2.0
%_prefix/share/gapi-2.0/gio-api.xml
