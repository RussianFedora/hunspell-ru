Name: hunspell-ru
Summary: Both English and Russian hunspell dictionaries
Version: 0.1
Release: 1%{?dist}
Epoch: 2
Source: rus-eng-myspell-%{version}.tar.bz2
Group: Applications/Text
URL: http://tigro.info
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: BSD
BuildArch: noarch

Requires: hunspell

%description
Both English and Russian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ru

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ru_RU-en_US.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ru_RU.dic
cp -p ru_RU-en_US.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ru_RU.aff


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README*
%{_datadir}/myspell/*

%changelog
* Thu Aug  7 2008 Arkady L. Shane <ashejn@yandex-team.ru - 1:0.1-1
- merge English and Russian (with ё) dictionaries
