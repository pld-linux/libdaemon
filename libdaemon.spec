#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Lightweight C library which eases the writing of UNIX daemons
Summary(pl):	Prosta biblioteka C u³atwiaj±ca pisanie demonów uniksowych
Name:		libdaemon
Version:	0.10
Release:	1
Epoch:		0
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
# Source0-md5:	6812a5e4063b5016f25e9a0cebbd3dd9
URL:		http://0pointer.de/lennart/projects/libdaemon/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	doxygen
BuildRequires:	lynx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdaemon is a lightweight C library which eases the writing of UNIX
daemons.

%description -l pl
libdaemon jest prost± bibliotek± C u³atwiaj±c± pisanie demonów
uniksowych.

%package devel
Summary:	Header files and development documentation for libdaemon
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty biblioteki libdaemon
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains Header files and development documentation for
libdaemon.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i dokumentacjê programisty
biblioteki libdaemon.

%package static
Summary:	Static libdaemon library
Summary(pl):	Statyczna biblioteka libdaemon
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static libdaemon library.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki libdaemon.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}
%{__make} doxygen

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a doc/reference/man/* $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
%{_mandir}/man?/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
