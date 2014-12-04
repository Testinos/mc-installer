Name:           double-conversion
Version:        master
Release:        1%{?dist}
Summary:        Binary-decimal and decimal-binary routines for IEEE doubles.
Group:          System Environment/Libraries
License:        The BSD 3-Clause License
URL:            https://code.google.com/p/double-conversion
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  scons

%description

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/double-conversion
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
cp src/*.h $RPM_BUILD_ROOT/%{_includedir}/double-conversion
cp -a libdouble-conversion*.so.* $RPM_BUILD_ROOT/%{_libdir}
cp -a libdouble-conversion*.a $RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libdouble-conversion.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libdouble-conversion.a
%{_libdir}/libdouble-conversion_pic.a
%{_includedir}/double-conversion/*
