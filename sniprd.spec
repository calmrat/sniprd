Name: status-report
Version: 0.4
Release: 1%{?dist}

Summary: Generate status report stats for selected date range
License: GPLv2+

URL: http://github.com/kejbaly2/sniprd
# FIXME: BORKED
Source0: http://github.com/kejbaly2/sniprd/%{name}-%{version}.tar.bz2

BuildArch: noarch
BuildRequires: python-devel
Requires: python-kerberos python-nitrate python-dateutil

%description
Comfortably generate status report stats (e.g. list of committed
changes) for given week, month, quarter, year or selected date
range. By default all available stats for this week are reported.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{python_sitelib}/status_report
mkdir -p %{buildroot}%{python_sitelib}/status_report/plugins
install -pm 755 source/status-report %{buildroot}%{_bindir}
install -pm 644 source/status_report/*.py %{buildroot}%{python_sitelib}/status_report
install -pm 644 source/status_report/plugins/*.py %{buildroot}%{python_sitelib}/status_report/plugins
install -pm 644 docs/_build/man/*.1.gz %{buildroot}%{_mandir}/man1

%files
%{_mandir}/man1/*
%{_bindir}/status-report
%{python_sitelib}/*
%doc README.rst examples
%{!?_licensedir:%global license %%doc}
%license LICENSE
