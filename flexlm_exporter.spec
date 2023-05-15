Name:           flexlm_exporter
Version:        0.0.8
Release:        1%{?dist}
Summary:        Prometheus exporter for FLEXlm License Manager lmstat license information.

License:        GPLv3
URL:		https://github.com/mjtrangoni/flexlm_exporter
Source0:        %{name}-%{version}.tar.gz
Source1:        licenses.yml
Source2:	%{name}.service

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
Prometheus exporter for FLEXlm License Manager lmstat license information.

%global debug_package %{nil}

%prep
%autosetup


%build
go build -v -o %{name}


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/licenses.yml
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

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


%changelog
* Wed May 19 2021 Patrik Pira - 0.0.8-1
- First release%changelog
