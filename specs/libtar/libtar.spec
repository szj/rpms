# $Id: $
# Authority: dries
# Upstream: Mark D. Roth <roth$feep,net>

Summary: C library for manipulating POSIX tar files.
Name: libtar
Version: 1.2.11
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.feep.net/libtar/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.feep.net/pub/software/libtar/libtar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel

%description
libtar is a C library for manipulating POSIX tar files. It handles adding
and extracting files to/from a tar archive.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL README TODO
%doc %{_mandir}/man?/*
%{_bindir}/libtar

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.11-1
- Initial package.
