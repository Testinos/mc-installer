Name:           ragel   
Summary:        Finite state machine compiler
Version:        6.9
Release:        2.3
Group:          Development/Tools
License:        GPLv2+
URL:            http://www.complang.org/%{name}/
Source0:        http://www.complang.org/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc, gcc-c++, libstdc++-devel
# for documentation building
BuildRequires:  transfig, tetex-latex, gcc-objc
Requires:       gawk

%description
Ragel compiles finite state machines from regular languages into executable C,
C++, Objective-C, or D code. Ragel state machines can not only recognize byte
sequences as regular expression machines do, but can also execute code at
arbitrary points in the recognition of a regular language. Code embedding is
done using inline operators that do not disrupt the regular language syntax.

%prep
%setup -q


%build
# set the names of the other programming commandline programs
%configure --docdir=%{_docdir}/%{name}-%{version} RUBY=ruby JAVAC=javac GMCS=gmcs 

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING ragel.vim
%doc doc/ragel-guide.pdf
%{_bindir}/ragel
%{_mandir}/*/*


%changelog
* Wed Jan 12 2011 Holger Manthey <holger.manthey@bertelsmann.de>
- initial packet
