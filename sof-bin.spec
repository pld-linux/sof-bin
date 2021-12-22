Summary:	Topology binaries for the Sound Open Firmware
Name:		sof-bin
Version:	2.0
Release:	1
License:	BSD/BSD-like/ISC
Group:		Base/Kernel
Source0:	https://github.com/thesofproject/sof-bin/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8d06ed4a1fba5fd77bb49bd35ddce757
URL:		https://github.com/thesofproject/sof-bin
BuildRequires:	rsync
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Topology binaries for the Sound Open Firmware.

%package -n sof-firmware
Summary:	Sound Open Firmware
Group:		Base/Kernel
BuildArch:	noarch

%description -n sof-firmware
Sound Open Firmware.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/firmware/intel,%{_bindir}}

FW_DEST=$RPM_BUILD_ROOT/lib/firmware/intel \
TOOLS_DEST=$RPM_BUILD_ROOT%{_bindir} \
./install.sh v2.0.x/v%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.Intel LICENCE.NXP Notice.NXP README.Intel
%attr(755,root,root) %{_bindir}/sof-*

%files -n sof-firmware
%defattr(644,root,root,755)
/lib/firmware/intel/sof*
