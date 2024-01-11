%define luaver 5.3
%define luapkgdir %{_datadir}/lua/%{luaver}
%global commit 7a86bc22066858afeb23845a191a6ab680b46233
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lua-json
Version:        1.3.2
Release:        9%{?dist}
Summary:        JSON Parser/Constructor for Lua
Group:          Development/Libraries
License:        MIT
URL:            http://luaforge.net/projects/luajson/
Source0:        https://github.com/harningt/luajson/archive/%{commit}/luajson-%{version}-%{shortcommit}.tar.gz
Patch0:		luajson-lua-5.2.patch
BuildRequires:  lua >= %{luaver}, lua-lpeg >= 0.8.1
# for checks
BuildRequires:  lua-filesystem >= 1.4.1, lua-lunit >= 0.4
Requires:       lua >= %{luaver}, lua-lpeg >= 0.8.1
BuildArch:      noarch

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

%prep
%setup -q -n luajson-%{commit}
%patch0 -p1 -b .lua-52

%build

%install
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
cp -pr lua/* $RPM_BUILD_ROOT%{luapkgdir}

%check
make check-regression
# three tests that used to fail here now pass because of how numbers work in lua 5.2
# make check-unit | tee testlog.txt
# grep -q "0 failed, 0 errors" testlog.txt

%files
%doc LICENSE docs/LuaJSON.txt docs/ReleaseNotes-1.0.txt
%{luapkgdir}/*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 20 2015 Bastien Nocera <bnocera@redhat.com> 1.3.2-5
- Rebuild for lua 5.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.3.2-1
- update to 1.3.2, rebuild for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Tom Callaway <spot@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 10 2009 Michel Salim <salimma@fedoraproject.org> - 1.0-1
- Initial package
