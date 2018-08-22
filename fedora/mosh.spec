Name:		mosh-af
Version:	1.3.2
Release:	1%{?dist}
Summary:	Mobile shell that supports roaming and intelligent local echo

License:	GPLv3+
Group:		Applications/Internet
URL:		https://mosh.mit.edu/
Source0:	https://github.com/kam1kaze/mosh/archive/af-%{version}.tar.gz

BuildRequires:	perl-generators
BuildRequires:	protobuf-compiler
BuildRequires:	protobuf-devel
BuildRequires:	libutempter-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
# autogen.sh required:
BuildRequires:	autoconf
BuildRequires:	automake

Requires:	openssh-clients
Requires:	openssl
Requires:	perl(IO::Socket::INET6)

%description
Mosh is a remote terminal application that supports:
  - intermittent network connectivity,
  - roaming to different IP address without dropping the connection, and
  - intelligent local echo and line editing to reduce the effects
    of "network lag" on high-latency connections.


%prep
%setup -q


%build
./autogen.sh
%configure --disable-silent-rules
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/mosh
%{_bindir}/mosh-client
%{_bindir}/mosh-server
%{_mandir}/man1/mosh.1.gz
%{_mandir}/man1/mosh-client.1.gz
%{_mandir}/man1/mosh-server.1.gz


%changelog
* Sun Mar 26 2017 Alex Chernyakhovsky <achernya@mit.edu> - 1.3.0-1
- Update to mosh 1.3.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.6-3
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.6-2
- Rebuild for protobuf 3.1.0

* Wed Aug 10 2016 Alex Chernyakhovsky <achernya@mit.edu> - 1.2.6-1
- Update to mosh 1.2.6

* Mon Feb 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2.5-3
- Let package honor RPM_OPT_FLAGS (Fix F24FTBFS).
- Add %%license.
- Make building verbose.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug  6 2015 Alex Chernyakhovsky <achernya@mit.edu> - 1.2.5-1
- Update to mosh 1.2.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Alex Chernyakhovsky <achernya@mit.edu> - 1.2.4-6
- Rebuild for protobuf version bump.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.4-2
- Perl 5.18 rebuild

* Wed Mar 27 2013 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2.4-1
- Update to mosh 1.2.4

* Sun Mar 10 2013 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2.3-3
- Rebuilt for Protobuf API change from 2.4.1 to 2.5.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2.3-1
- Update to mosh 1.2.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2.2-1
- Update to mosh 1.2.2

* Sat Apr 28 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2-2
- Add -g and -O2 CFLAGS

* Fri Apr 27 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.2-1
- Update to mosh 1.2.

* Mon Mar 26 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.1.1-1
- Update to mosh 1.1.1.

* Wed Mar 21 2012 Alexander Chernyakhovsky <achernya@mit.edu> - 1.1-1
- Initial packaging for mosh.
