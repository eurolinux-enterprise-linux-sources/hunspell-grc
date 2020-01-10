Name: hunspell-grc
Summary: Ancient Greek hunspell dictionaries
Version: 2.1.5
Release: 7%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/e-files/2313/1/grc.oxt
URL: http://www.himeros.eu/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+ or LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Ancient Greek hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/grc_GR.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/grc.aff
cp -p dictionaries/grc_GR.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/grf.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSES-en.txt         

%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.1.5-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Caolan McNamara <caolanm@redhat.com> - 2.1.5-4
- Resolves: rhbz#803081 drop TERRITORY

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Caolan McNamara <caolanm@redhat.com> - 2.1.5-1
- latest version

* Wed Oct 14 2009 Caolan McNamara <caolanm@redhat.com> - 2.1.4-0.1.alpha
- initial version
