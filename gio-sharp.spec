Summary:	.NET/C Sharp Bindings for GIO
Name:		gio-sharp
Version:	0.3
Release:	1
License:	GPLv2 and MIT
Group:		Development/Other
Url:		https://github.com/mono/gio-sharp
Source0:	https://github.com/mono/gio-sharp/archive/refs/tags/%{version}.tar.gz
Patch0:		https://github.com/mono/gio-sharp/commit/a9468300a2b3de749d1e85746ccab65241be28c1.patch
BuildArch:	noarch

BuildRequires:  monodoc-core
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(mono)
Requires:	glib2 > 2.22
#gw strictly speaking, it needs libgio:
Requires:	gvfs

%description
C#/CLI bindings for GIO

%package devel
Group:		Development/Other
Summary:	.NET/C# Bindings for GIO
Requires:	%{name} = %{version}-%{release}

%description devel
Files for developing programs that use gio-sharp

%prep
%autosetup -p1
%configure --libdir=%{_prefix}/lib

%build
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc AUTHORS NEWS README
#ChangeLog 
%dir %{_prefix}/lib/gio-sharp
%{_prefix}/lib/gio-sharp/gio-sharp.dll*

%files devel
%{_datadir}/pkgconfig/gio-sharp-2.0.pc
%dir %{_prefix}/share/gapi-2.0
%{_prefix}/share/gapi-2.0/gio-api.xml
