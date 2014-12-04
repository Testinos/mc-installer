Name:           glog
Version:        0.3.3
Release:        8%{?dist}
Summary:        A C++ application logging library

Group:          System Environment/Libraries
License:        BSD
URL:            http://code.google.com/p/google-glog
Source0:        http://google-glog.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Patch0:		glog-0.3.3-gflags-namespace.patch

BuildRequires:  autoconf, gflags-devel >= 2.1.0
Requires:       gflags

%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -p1 -P 0

%build
autoconf
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{_libdir}/libglog.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/designstyle.css doc/glog.html
%{_libdir}/libglog.so
%{_libdir}/pkgconfig/libglog.pc
%dir %{_includedir}/glog
%{_includedir}/glog/*


%changelog
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 John Khvatov <ivaxer@fedoraproject.org> - 0.3.3-6
- Rebuild against gflags.so.2.1

* Thu Apr 24 2014 Dan Fuhry <dfuhry@dattobackup.com> - 0.3.3-4
- Added patch for compatibility with gflags >= 2.1.0.

* Mon Aug 05 2013 John Khvatov <ivaxer@fedoraproject.org> - 0.3.3-3
- Removed installed but untracked docs.
   Fix for https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 John Khvatov <ivaxer@fedoraproject.org> - 0.3.3-1
- update to 0.3.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 03 2009 John A. Khvatov <ivaxer@fedoraproject.org> - 0.3.0-1
- update to 0.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 John A. Khvatov <ivaxer@fedoraproject.org> 0.2-5
- fixes for gcc 4.4

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 John A. Khvatov <ivaxer@fedoraproject.org> 0.2-2
- update to 0.2

* Thu Dec 4 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-6
- fix %%{_includedir}
- fixed documentation

* Wed Dec 3 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-5
- Added configure regeneration

* Tue Dec 2 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-4
- Initial release
