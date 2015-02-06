Summary:	Touch Typing Tutor
Name:		klavaro
Version:	1.9.3
Release:	3
License:	GPLv2+
Group:		Education
Source0:	http://downloads.sourceforge.net/project/klavaro/%name-%version.tar.bz2
Patch0:		klavaro-1.9.1-ru.patch
URL:		http://klavaro.sourceforge.net
Suggests:	wget
BuildRequires:	pkgconfig(gtk+-2.0)
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
%configure2_5x LIBS="-lgmodule-2.0"
%make

%install
%makeinstall_std

%{find_lang} %{name}

#mkdir -p %buildroot%_datadir/applications/
#cat > %buildroot%_datadir/applications/mandriva-%{name}.desktop <<EOF
#[Desktop Entry]
#Type=Application
#Exec=%_bindir/%name
#Name=Klavaro
#Comment=Touch Typing Tutor
#Icon=klavaro
#Categories=Education;ComputerScience;GTK;
#EOF

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*.1.*


%changelog
* Fri Aug 12 2011 Александр Казанцев <kazancas@mandriva.org> 1.9.3-2mdv2012.0
+ Revision: 694280
- fix double .desktop file

* Fri Jul 22 2011 Александр Казанцев <kazancas@mandriva.org> 1.9.3-1
+ Revision: 690930
- new verison 1.9.3

* Mon Jun 27 2011 Tomas Kindl <supp@mandriva.org> 1.9.2-1
+ Revision: 687533
- update to 1.9.2

* Fri May 20 2011 Александр Казанцев <kazancas@mandriva.org> 1.9.1-1
+ Revision: 676436
- new version 1.9.1

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 1.7.3-1mdv2011.0
+ Revision: 598557
- update to new version 1.7.3

* Mon Sep 20 2010 Tomas Kindl <supp@mandriva.org> 1.7.1-1mdv2011.0
+ Revision: 580260
- bump to 1.7.1

* Wed Aug 25 2010 Funda Wang <fwang@mandriva.org> 1.7.0-1mdv2011.0
+ Revision: 573021
- update to new version 1.7.0

* Sun Feb 28 2010 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2010.1
+ Revision: 512709
- New version 1.5.0

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 485086
- update to new version 1.4.1

* Sat Nov 28 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.0-1mdv2010.1
+ Revision: 470986
- update to new version 1.4.0

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 1.3.6-2mdv2010.1
+ Revision: 466169
- rebuild for new gtkdatabox

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.6-1mdv2010.1
+ Revision: 462695
- update to new version 1.3.6

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.1-2mdv2010.0
+ Revision: 455873
- rebuild for new curl SSL backend

* Mon Sep 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 440694
- update to new version 1.3.1

* Mon Aug 03 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.2-1mdv2010.0
+ Revision: 408489
- update to new version 1.2.2

* Tue Jun 16 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.1-1mdv2010.0
+ Revision: 386426
- update to new version 1.2.1

* Wed May 20 2009 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2010.0
+ Revision: 377895
- update tarball
- add BR
- New version 1.2.0

* Sat May 02 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.9-1mdv2010.0
+ Revision: 370809
- update to new version 1.1.9

* Wed Dec 10 2008 Funda Wang <fwang@mandriva.org> 1.1.8-1mdv2009.1
+ Revision: 312442
- br curl
- new version 1.1.8

* Sat Oct 18 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1.7-1mdv2009.1
+ Revision: 295038
- update to new version 1.1.7

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 1.1.6-1mdv2009.1
+ Revision: 292830
- update to new version 1.1.6

* Sun Sep 07 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1.5-1mdv2009.0
+ Revision: 282104
- update to new version 1.1.5

* Sun Aug 17 2008 Funda Wang <fwang@mandriva.org> 1.1.4-1mdv2009.0
+ Revision: 273096
- New version 1.1.4

* Tue Aug 12 2008 Funda Wang <fwang@mandriva.org> 1.1.3-1mdv2009.0
+ Revision: 271217
- New version 1.1.3

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2009.0
+ Revision: 257073
- New version 1.1.2

* Sat Jun 28 2008 Funda Wang <fwang@mandriva.org> 1.1.1-1mdv2009.0
+ Revision: 229725
- update to new version 1.1.1

* Tue Jun 17 2008 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2009.0
+ Revision: 222090
- update to new version 1.1.0

* Mon Jun 16 2008 Funda Wang <fwang@mandriva.org> 1.0.9-1mdv2009.0
+ Revision: 219566
- import klavaro


