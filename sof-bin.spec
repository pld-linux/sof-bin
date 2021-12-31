
%define		sof_ver		2.0
%define		sof_ver_pkg	v%{sof_ver}.x

Summary:	Topology binaries for the Sound Open Firmware
Name:		sof-bin
Version:	%{sof_ver}
Release:	2
License:	BSD/BSD-like/ISC
Group:		Base/Kernel
Source0:	https://github.com/thesofproject/sof-bin/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8d06ed4a1fba5fd77bb49bd35ddce757
URL:		https://github.com/thesofproject/sof-bin
BuildRequires:	alsa-lib
BuildRequires:	alsa-utils
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
mkdir -p firmware/intel/sof
mv %{sof_ver_pkg}/sof-v%{version}/* firmware/intel/sof
mv %{sof_ver_pkg}/sof-tplg-v%{version} firmware/intel/sof-tplg

%build
# SST topology files (not SOF related, but it's a Intel hw support
# and this package seems a good place to distribute them
alsatplg -c /usr/share/alsa/topology/hda-dsp/skl_hda_dsp_generic-tplg.conf \
	-o firmware/skl_hda_dsp_generic-tplg.bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/firmware/intel,%{_bindir}}

cp -ra %{sof_ver_pkg}/tools-v%{version}/* $RPM_BUILD_ROOT%{_bindir}
cp -ra firmware/* $RPM_BUILD_ROOT/lib/firmware/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.Intel LICENCE.NXP Notice.NXP README.Intel
%attr(755,root,root) %{_bindir}/sof-*

%files -n sof-firmware
%defattr(644,root,root,755)
/lib/firmware/*.bin
/lib/firmware/intel/sof
/lib/firmware/intel/sof-tplg
# exclude debug data
%exclude /lib/firmware/intel/sof/*.ldc
%exclude /lib/firmware/intel/sof/*/*.ldc
