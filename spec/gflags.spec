%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           gflags
Version:        2.1.1
Release:        6%{?dist}
Summary:        Library for commandline flag processing

Group:          Development/Tools
License:        BSD
URL:            http://code.google.com/p/%{name}
Source0:        http://github.com/schuhschuh/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         gflags-0001-cmake-append-LIB_SUFFIX-to-LIBRARY_INSTALL_DIR.patch
Patch1:         gflags-0001-Set-VERSION-property-of-library-targets-to-major.patch
BuildRequires:  python-setuptools
BuildRequires:  cmake

%description
The gflags package contains a library that implements commandline
flags processing. As such it's a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .lib_suffix
%patch1 -p1 -b .lib_version

%build
%cmake -DBUILD_TESTING:BOOL=OFF .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%check
ctest

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ChangeLog.txt README.txt COPYING.txt AUTHORS.txt
%{_bindir}/gflags_completions.sh
%{_libdir}/libgflags.so.*
%{_libdir}/libgflags_nothreads.so.*

%files devel
%doc doc/designstyle.css doc/gflags.html
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libgflags.so
%{_libdir}/libgflags_nothreads.so
%dir %{_libdir}/cmake
%{_libdir}/cmake/%{name}

%changelog
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.1.1-5
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 John Khvatov <ivaxer@fedoraproject.org> - 2.1.1-3
- Add patch (from upstream) for shared library versining.

* Wed Apr 30 2014 John Khvatov <ivaxer@fedoraproject.org> - 2.1.1-2
- Enable test suite
- Update SourceURL (upstream moved to github)
- Add patch to use LIB_SUFFIX in cmake configs
- Spec cleanup

* Wed Apr 23 2014 Dan Fuhry <dfuhry@dattobackup.com> - 2.1.1-1
- Updated to 2.1.1

* Sat Aug 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3-8
- Use system-wide libtool
- Autoregen everything

* Tue Aug 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3-7
- Cleanup spec-file (removed EL6/FC6 stuff)
- Fix doc-files installation

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 30 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.3-1
- Updated to 1.3
- Removed python bindings (they are separate project now)

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2-1
- Updated to 1.2

* Wed Aug 05 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.1-1
- removed extra files included in %%files section and updated to 1.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Debarshi Ray <rishi@fedoraproject.org> - 1.0-3
- Fixed build failure with gcc-4.4.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.0-1
- Updated to 1.0.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9-7
- Rebuild for Python 2.6

* Thu Sep 04 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.9-6
- fixed for F-8 provide eggs for non setuptools package

* Thu Sep 04 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.9-5
- disable test suite because it failed on x86_64 (2/17)

* Tue Aug 26 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.9-4
- fixed %%{includedir}

* Thu Aug 14 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.9-3
- fixed documentation, timestamp saving
- removed chrpath & cleaned some unwanted commands
- included python module

* Sat Aug 09 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.9-2
- remove automake and corrected configure option

* Thu Aug 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.9-1
- Initial build
