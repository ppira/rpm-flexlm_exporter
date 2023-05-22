Name:           flexlm_exporter
Version:        0.0.9
Release:        1%{?dist}
Summary:        Prometheus exporter for FLEXlm License Manager lmstat license information.

License:        GPLv3
URL:		https://github.com/mjtrangoni/flexlm_exporter/archive/refs/heads/master.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        licenses.yml
Source2:	%{name}.service
Source3:	%{name}.xml

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
Prometheus exporter for FLEXlm License Manager lmstat license information.

%global debug_package %{nil}

%prep
curl -L %{url} -o %{name}-%{version}.tar.gz
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
gzip -dc ../%{name}-%{version}.tar.gz |tar --strip-components 1 -xof -


%build
cd %{name}-%{version}
go build -v -o %{name}


%install
cd %{name}-%{version}
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/licenses.yml
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml

%check
# go test should be here... :)

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%dir %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}/licenses.yml
%{_prefix}/lib/firewalld/services/%{name}.xml


%changelog
* Wed May 22 2021 Patrik Pira - 0.0.9-1
- Build from git master
 
* Wed May 19 2021 Patrik Pira - 0.0.8-1
- First release%changelog
