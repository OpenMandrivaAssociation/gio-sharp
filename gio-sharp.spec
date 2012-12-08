Name:		gio-sharp
Version:	2.22.3
Release:	1
License:	GPLv2 and MIT
Group:		Development/Other
Summary:	.NET/C# Bindings for GIO
Url:		https://github.com/mono/gio-sharp
Source:		https://github.com/downloads/mono/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  glib-sharp2
BuildRequires:  gtk-sharp2-devel
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
Requires:	glib2 > 2.22
#gw strictly speaking, it needs libgio:
Requires:	gvfs
BuildArch:	noarch

%description
C#/CLI bindings for GIO

%package devel
Group:		Development/Other
Summary:	.NET/C# Bindings for GIO
Requires:	%{name} = %{version}-%{release}

%description devel
Files for developing programs that use gio-sharp

%prep
%setup -q

%build
%configure2_5x --libdir=%{_prefix}/lib
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc AUTHORS NEWS README
#ChangeLog 
%dir %{_prefix}/lib/gio-sharp
%{_prefix}/lib/gio-sharp/gio-sharp.dll*

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/gio-sharp-2.0.pc
%dir %_prefix/share/gapi-2.0
%_prefix/share/gapi-2.0/gio-api.xml


%changelog
* Thu Nov 03 2011 Götz Waschk <waschk@mandriva.org> 2.22.3-0.3mdv2012.0
+ Revision: 716264
- really add new version
- fix build
- update file list
- new version
- new URL

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.22-0.2
+ Revision: 664845
- mass rebuild

* Sat Aug 07 2010 Götz Waschk <waschk@mandriva.org> 2.22-0.1mdv2011.0
+ Revision: 567377
- import gio-sharp


