
Summary:	Bluemote - a remote controller for your PC via bluetooth
Summary(pl):	Bluemote - pilot dla komputera via bluetooth
Name:		bluemote
Version:	2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.geocities.com/saravkrish/progs/bluemote/%{name}.%{version}.tar.gz
# Source0-md5:	69ab4eafb839a3f22fca2832fbba60f6
URL:		http://www.geocities.com/saravkrish/progs/bluemote/
Requires:	bluez-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluemote is a program meant to extend your Bluetooth enabled T610 (and
most other Sony Ericsson) as a remote for your PC.

%description -l pl
Bluemote to program, który zamieni wyposa¿ony w Bluetooth telefon T610
(i wiêkszo¶æ innych telefonów Sony Ericsson) w pilota dla komputera.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install bluemote $RPM_BUILD_ROOT%{_bindir}/bluemoteapp
install bluemote-example.cfg $RPM_BUILD_ROOT%{_datadir}/%{name}/bluemote.cfg

cat > $RPM_BUILD_ROOT%{_bindir}/bluemote <<EOF
#!/bin/sh
[ -e ~/.bluemote.cfg ] ||
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
%{_datadir}/%{name}/bluemote.cfg
