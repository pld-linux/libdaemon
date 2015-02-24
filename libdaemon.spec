#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Lightweight C library which eases the writing of UNIX daemons
Summary(pl.UTF-8):	Prosta biblioteka C ułatwiająca pisanie demonów uniksowych
Name:		libdaemon
Version:	0.14
Release:	2
Epoch:		0
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
# Source0-md5:	509dc27107c21bcd9fbf2f95f5669563
URL:		http://0pointer.de/lennart/projects/libdaemon/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	libtool
BuildRequires:	doxygen
BuildRequires:	lynx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdaemon is a lightweight C library which eases the writing of UNIX
daemons.

%description -l pl.UTF-8
libdaemon jest prostą biblioteką C ułatwiającą pisanie demonów
uniksowych.

%package devel
Summary:	Header files and development documentation for libdaemon
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programisty biblioteki libdaemon
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains Header files and development documentation for
libdaemon.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i dokumentację programisty
biblioteki libdaemon.

%package static
Summary:	Static libdaemon library
Summary(pl.UTF-8):	Statyczna biblioteka libdaemon
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static libdaemon library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki libdaemon.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
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
%attr(755,root,root) %{_libdir}/libdaemon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdaemon.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdaemon.so
%{_libdir}/libdaemon.la
%{_includedir}/%{name}
%{_pkgconfigdir}/libdaemon.pc
%{_mandir}/man3/daemon.h.3*
%{_mandir}/man3/dexec.h.3*
%{_mandir}/man3/dfork.h.3*
%{_mandir}/man3/dlog.h.3*
%{_mandir}/man3/dnonblock.h.3*
%{_mandir}/man3/dpid.h.3*
%{_mandir}/man3/dsignal.h.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdaemon.a
%endif
