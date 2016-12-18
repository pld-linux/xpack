Summary:	Library for experimental XPACK compression format
Summary(pl.UTF-8):	Biblioteka do eksperymentalnego formatu kompresji XPACK
Name:		xpack
Version:	0.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ebiggers/xpack/releases
Source0:	https://github.com/ebiggers/xpack/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2d73e67ac8c8659de3a5e5fea4fb58fd
Patch0:		%{name}-soname.patch
URL:		https://github.com/ebiggers/xpack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XPACK is an experimental compression format. It is intended to have
better performance than DEFLATE as implemented in the zlib library and
also produce a notably better compression ratio on most inputs. The
format is not yet stable.

%description -l pl.UTF-8
XPACK to eksperymentalny format kompresji. Jego celem jest lepsza
wydajność od algorytmu DEFLATE zaimplementowanego w bibliotece zlib
oraz uzyskanie znacząco lepszego współczynnika kompresji na większości
danych wejściowych. Format jeszcze nie jest stabilny.

%package devel
Summary:	Header file for xpack library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki xpack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for xpack library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki xpack.

%package static
Summary:	Static xpack library
Summary(pl.UTF-8):	Statyczna biblioteka xpack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xpack library.

%description static -l pl.UTF-8
Statyczna biblioteka xpack.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install xpack xunpack $RPM_BUILD_ROOT%{_bindir}
install libxpack.so $RPM_BUILD_ROOT%{_libdir}/libxpack.so.0
ln -sf libxpack.so.0 $RPM_BUILD_ROOT%{_libdir}/libxpack.so
cp -p libxpack.a $RPM_BUILD_ROOT%{_libdir}
cp -p libxpack.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_bindir}/xpack
%attr(755,root,root) %{_bindir}/xunpack
%attr(755,root,root) %{_libdir}/libxpack.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxpack.so
%{_includedir}/libxpack.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxpack.a
