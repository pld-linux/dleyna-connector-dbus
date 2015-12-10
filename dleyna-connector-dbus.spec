Summary:	D-Bus connector for dLeyna services
Name:		dleyna-connector-dbus
Version:	0.2.0
Release:	1
License:	LGPL v2
Group:		Applications
Source0:	https://01.org/sites/default/files/downloads/dleyna/%{name}-%{version}.tar.gz
# Source0-md5:	04c2425239d092f4da457c061be7aa81
Patch0:		0001-Connector-Don-t-crash-when-trying-to-unwatch-non-exi.patch
URL:		https://01.org/dleyna/
BuildRequires:	autoconf >= 2.66
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	dleyna-core-devel >= 0.2.1
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.16
Requires:	dbus
Requires:	dleyna-core >= 0.2.1
Requires:	glib2 >= 1:2.28.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Bus connector for dLeyna services.

%package devel
Summary:	Development files for dleyna-connector-dbus
Group:		Development/Libraries
Requires:	dbus-devel
Requires:	glib2-devel >= 1:2.28.0

%description devel
This package provides development files for dleyna-connector-dbus.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/dleyna-1.0/connectors/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/dleyna-1.0/connectors/libdleyna-connector-dbus.so

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/dleyna-connector-dbus-1.0.pc
