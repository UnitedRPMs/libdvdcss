Summary: A portable abstraction library for DVD decryption
Name: libdvdcss
Version: 1.4.2
Release: 2%{?dist}
License: GPLv2
Group: System Environment/Libraries
Source: http://download.videolan.org/pub/videolan/libdvdcss/%{version}/libdvdcss-%{version}.tar.bz2
URL: http://www.videolan.org/libdvdcss/
BuildRequires: gcc-c++
Provides: dvdcss-libs = %{version}-%{release}

%package devel
Summary:	Development files for the libdvdcss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the libdvdcss

%description
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.

%prep
%setup -q

%build
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/libdvdcss.so.*
# {_docdir}/libdvdcss/ChangeLog

%files devel
%defattr(-,root,root,-)
%{_includedir}/dvdcss
%{_libdir}/libdvdcss.so
%{_libdir}/pkgconfig/libdvdcss.pc

%changelog

* Fri Mar 23 2018 David Vasquez <davidva at tutanota dot com> 1.4.2-2
- Updated to 1.4.2

* Tue Jan 09 2018 David Vasquez <davidva at tutanota dot com> 1.4.1-2
- Updated to 1.4.1 

* Thu Apr 28 2016 David Vasquez <davidjeremias82 at gmail dot com> 1.4.0-2
- Rebuilt 

* Sat Apr 02 2016 David Vasquez <davidjeremias82 at gmail dot com> 1.4.0-1
- Updated to 1.4.0

* Thu Oct 01 2015 David Vasquez <davidjeremias82 at gmail dot com> 1.3.99-2
- Rebuilt

* Wed Apr 15 2015 David Vasquez <davidjeremias82 at gmail dot com> 1.3.99-1
- Updated to 1.3.99

* Mon Oct 06 2014 David Vásquez <davidjeremias82 AT gmail DOT com> 1.3.0
- Initial RPM release.
