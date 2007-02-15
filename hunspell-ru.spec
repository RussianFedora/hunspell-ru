Name: hunspell-ru
Summary: Russian hunspell dictionaries
%define upstreamid 20040406
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/ru_RU.zip
Group: Applications/Text
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: BSD
BuildArch: noarch

Requires: hunspell

%description
Russian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ru

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ru_RU.txt
%{_datadir}/myspell/*

%changelog
* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040406-1
- initial version
