Name: hunspell-ru
Summary: Russian hunspell dictionaries
Version: 0.99f7
Release: 1%{?dist}
Epoch: 1
Source: ftp://ftp.vsu.ru/mirrors/scon155.phys.msu.su/pub/russian/ispell/myspell/rus-myspell-%{version}.tar.gz
Group: Applications/Text
URL: ftp://scon155.phys.msu.su/pub/russian/ispell/myspell
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
cp -p ru_myspell.dict $RPM_BUILD_ROOT/%{_datadir}/myspell/ru_RU.dic
cp -p ru_RU.koi8r.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ru_RU.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE readme.koi
%{_datadir}/myspell/*

%changelog
* Tue Aug 21 2007 Caolan McNamara <caolanm@redhat.com> - 1:0.99f7-1
- clarify licence
- canonical upstream source

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040406-1
- initial version
