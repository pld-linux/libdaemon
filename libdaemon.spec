Summary:	Lightweight C library which eases the writing of UNIX daemons
Summary(pl):	Prosta biblioteka C u�atwiaj�ca pisanie demon�w uniksowych
Name:		libdaemon
Version:	0.2
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.stud.uni-hamburg.de/~lennart/projects/libdaemon/libdaemon-0.2.tar.gz
# Source0-md5:	e75d2907a38d13e72091d147ef454cbd
URL:		http://www.stud.uni-hamburg.de/~lennart/projects/libdaemon/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdaemon is a lightweight C library which eases the writing of UNIX
daemons.

%description -l pl
libdaemon jest prost� bibliotek� C u�atwiaj�c� pisanie demon�w
uniksowych.

%package devel
Summary:	Header files and develpment documentation for libdaemon
Summary(pl):	Pliki nag��wkowe i dokumentacja programisty biblioteki libdaemon
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
This package contains Header files and develpment documentation for
libdaemon.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe i dokumentacj� programisty
biblioteki libdaemon.

%package static
Summary:	Static libdaemon library
Summary(pl):	Statyczna biblioteka libdaemon
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
This package contains static libdaemon library.

%description static -l pl
Ten pakiet zawiera statyczn� wersj� biblioteki libdaemon.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a doc/reference/man/* $RPM_BUILD_ROOT%{_mandir}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
