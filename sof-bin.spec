Summary:	Topology binaries for the Sound Open Firmware
Name:		sof-bin
Version:	2023.09
Release:	2
License:	BSD/BSD-like/ISC
Group:		Base/Kernel
Source0:	https://github.com/thesofproject/sof-bin/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3e4fcbe214a585e63d43c4b0df4cbd78
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
mkdir -p firmware/intel
%{__mv} sof firmware/intel/sof
%{__mv} sof-ace-tplg firmware/intel/sof-ace-tplg
%{__mv} sof-ipc4 firmware/intel/sof-ipc4
%{__mv} sof-tplg firmware/intel/sof-tplg

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      tools/mtrace-reader.py

%build
# SST topology files (not SOF related, but it's a Intel hw support
# and this package seems a good place to distribute them
alsatplg -c /usr/share/alsa/topology/hda-dsp/skl_hda_dsp_generic-tplg.conf \
	-o firmware/skl_hda_dsp_generic-tplg.bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/firmware/intel,%{_bindir}}

cp -ra tools/* $RPM_BUILD_ROOT%{_bindir}
cp -ra firmware/* $RPM_BUILD_ROOT/lib/firmware/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE.Intel LICENCE.NXP Notice.NXP README.Intel
%attr(755,root,root) %{_bindir}/mtrace-reader.py
%attr(755,root,root) %{_bindir}/sof-*

%files -n sof-firmware
%defattr(644,root,root,755)
/lib/firmware/*.bin
/lib/firmware/intel/sof
/lib/firmware/intel/sof-ace-tplg
/lib/firmware/intel/sof-ipc4
/lib/firmware/intel/sof-tplg
