Summary:	Touch Typing Tutor
Name:		klavaro
Version:	1.9.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Education
Source0:	http://downloads.sourceforge.net/project/klavaro/%name-%version.tar.bz2
Patch0:		klavaro-1.9.1-ru.patch
URL:		http://klavaro.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}
Suggests:	wget
BuildRequires:	gtk+2-devel
BuildRequires:	gtkdatabox-devel
BuildRequires:	libsexy-devel
BuildRequires:	curl-devel intltool

%description
Klavaro is just another free touch typing tutor program. We felt like to
do it because we became frustrated with the other options, which relied
mostly on some few specific keyboards. Klavaro intends to be keyboard
and language independent, saving memory and time (and money).

%prep
%setup -q
%patch0 -p0 -b .ru

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

mkdir -p %buildroot%_datadir/applications/
cat > %buildroot%_datadir/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=%_bindir/%name
Name=Klavaro
Comment=Touch Typing Tutor
Icon=klavaro
Categories=Education;ComputerScience;GTK;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*.1.*
