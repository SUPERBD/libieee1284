Summary:	A library for interfacing IEEE 1284-compatible devices
Summary(pl):	Biblioteka do komunikacji z urządzeniami kompatybilnymi z IEEE 1284
Name:		libieee1284
Version:	0.2.9
%define		_pre pre2
Release:	0.%{_pre}.1
License:	GPL
Group:		Libraries
Source0:	http://cyberelk.net/tim/data/libieee1284/stable/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	d9682040b3cb3bf8ece7f104cbb11dcd
URL:		http://cyberelk.net/tim/libieee1284/index.html
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	libtool
BuildRequires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libieee1284 library is for communicating with parallel port
devices.

%description -l pl
Biblioteka libieee1284 służy do komunikacji z urządzeniami
podłączanymi do portu równoległego.

%package devel
Summary:	Files for developing applications that use libieee1284
Summary(pl):	Pliki do tworzenia programów używających libieee1284
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The header files, libtool library and man pages for developing
applications that use libieee1284.

%description devel -l pl
Pliki nagłówkowe i dokumentacja do tworzenia programów używających
libieee1284.

%package static
Summary:	Static version of libieee1284
Summary(pl):	Statyczna wersja libieee1284
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libieee1284 library.

%description static -l pl
Statyczna wersja biblioteki libieee1284.

%package -n python-ieee1284
Summary:	Python binding for libieee1284 library
Summary(pl):	Wiązanie Pythona dla biblioteki libieee1284
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-ieee1284
Python binding for libieee1284 library.

%description -n python-ieee1284 -l pl
Wiązanie Pythona dla biblioteki libieee1284.

%prep
%setup -q -n %{name}-%{version}%{_pre}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/libieee1284_test
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ieee1284.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n python-ieee1284
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/ieee1284module.so
