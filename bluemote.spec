Summary:	Bluemote - a remote controller for your PC via Bluetooth
Summary(de.UTF-8):   Bluemote - Bluetooth Fernbedienung für den PC
Summary(pl.UTF-8):   Bluemote - pilot dla komputera przez Bluetooth
Name:		bluemote
Version:	2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.geocities.com/saravkrish/progs/bluemote/%{name}.%{version}.tar.gz
# Source0-md5:	69ab4eafb839a3f22fca2832fbba60f6
URL:		http://www.geocities.com/saravkrish/progs/bluemote/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	bluez-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluemote is a program meant to extend your Bluetooth enabled T610 (and
most other Sony Ericsson) as a remote for your PC.

%description -l de.UTF-8
Bluemote ist ein Programm, dass dein T610 Bluetooth Handy (und andere
Sony Ericsson Modelle) in eine Komputerfernbedienung verwandelt.

%description -l pl.UTF-8
Bluemote to program, który zamieni wyposażony w Bluetooth telefon T610
(i większość innych telefonów Sony Ericsson) w pilota dla komputera.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	X11FLAGS="-lX11 -lXtst"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install bluemote $RPM_BUILD_ROOT%{_bindir}/bluemoteapp
install bluemote-example.cfg $RPM_BUILD_ROOT%{_datadir}/%{name}/bluemote.cfg

cat > $RPM_BUILD_ROOT%{_bindir}/bluemote <<EOF
#!/bin/sh
[ -e ~/.bluemote.cfg ] || \
	/bin/cp -a %{_datadir}/%{name}/bluemote.cfg ~/.bluemote.cfg

exec %{_bindir}/bluemoteapp

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR README config.txt
%attr(755,root,root) %{_bindir}/bluemoteapp
%attr(755,root,root) %{_bindir}/bluemote
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bluemote.cfg
