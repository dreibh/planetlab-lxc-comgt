%define name comgt
%define version 0.3
%define subversion 1

%define release %{subversion}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

Summary: GPRS/EDGE/3G/HSDPA datacard control tool 
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System Environment/Kernel
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Vendor: OneLab
Packager: OneLab <support@one-lab.org>
Distribution: OneLab %{version}
URL: http://www.pharscape.org/content/view/46/70/

%description
comgt allows to monitor and set various settings into a UMTS card

%prep
%setup

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D -m 755 gcom $RPM_BUILD_ROOT/usr/sbin/gcom 
install -D -m 755 sigmon $RPM_BUILD_ROOT/usr/sbin/sigmon 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/sbin/gcom
/usr/sbin/sigmon

%changelog
* Wed Jul 04 2007 Thierry Parmentelat <thierry.parmentelat@sophia.inria.fr> - 0.3-1
- creation
