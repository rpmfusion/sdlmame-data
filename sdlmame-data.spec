%define vernumber 140

Name:           sdlmame-data
Version:        0%{vernumber}
Release:        1%{?dist}
Summary:        Data files for the SDLMAME package

Group:          Amusements/Games
License:        Distibutable
URL:            http://mamedev.org
Source1:        http://www.arcade-history.com/dats/mamehistory%{vernumber}.7z
Source2:        http://www.mameworld.info/mameinfo/download/Mameinfo%{version}.zip
Source3:        http://www.kutek.net/mame_roms_pinball/mame32_config_files/ctrlr.rar
Source4:        http://www.progettoemma.net/public/cat/catveren.zip
Source5:        http://nplayers.arcadebelgium.be/files/nplayers%{version}.zip
Source6:        http://cheat.retrogames.com/download/cheat%{version}.7z
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  p7zip
BuildRequires:  unrar

Requires:       sdlmame >= %{version}

%description
%{summary}.

%prep
%setup -qcT

# extract DAT files
7za x %{SOURCE1}
7za x %{SOURCE2}
7za x Mameinfo%{version}.exe
mv docs mameinfo
unzip -qa %{SOURCE4} -d .
unzip -qa %{SOURCE5} -d .
mv docs nplayers
7za x %{SOURCE6}

# fix permissions and line endings
chmod 0644 mameinfo/*.txt
chmod 0755 mameinfo
sed -i 's/\r//' cheat.txt readhist.txt readme.txt mameinfo/* nplayers/nplayers.txt 

#fix encoding
for i in readhist.txt mameinfo/*.txt
do
/usr/bin/iconv -f iso8859-1 -t utf-8 $i > $i.conv && /bin/mv -f $i.conv $i;
done


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mame
install -pm 644 history.dat mameinfo.dat Catver.ini nplayers.ini cheat.zip\
    $RPM_BUILD_ROOT%{_datadir}/mame
install -d $RPM_BUILD_ROOT%{_datadir}/mame/ctrlr
unrar x %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mame


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc nplayers/nplayers.txt mameinfo cheat.txt readhist.txt readme.txt
%{_datadir}/mame


%changelog
* Sun Oct 24 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0140-1
- Updated to 0.140

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0139-2
- rebuilt

* Wed Aug 04 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0139-1
- Updated to 0.139

* Sat May 29 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0138-1
- Updated to 0.138 (except cheats)
- Fixed Source2 and Source6 Source URLs

* Thu Mar 25 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0137-1
- Updated to 0.137

* Fri Jan 08 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0136-1
- Updated to 0.136
- Dropped the workaround, it was not helping anyway

* Sat Nov 21 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0135-1
- Updated everything except cheats to 0.135
- Worked around RPM Fusion bug #956

* Thu Sep 17 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0134-1
- Updated to 0.134
- Switched to 7z sources for history.dat

* Mon Aug 03 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0133-1
- Updated everything except cheats to 0.133

* Sun Jun 14 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0132-1
- Updated to 0.132

* Thu Apr 30 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0131-2
- Updated cheats to 0.131

* Sun Apr 26 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0131-1
- Updated mameinfo.dat to 0.131
- Updated history.dat to 0.131
- Updated catver.ini to 0.131
- Updated nplayers.ini to 0.131

* Fri Apr 03 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0130-3
- Added cheats back, now in the form of the xml files

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0130-2
- rebuild for new F11 features

* Thu Mar 12 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0130-1
- Updated mameinfo.dat to 0.130 and updated the Source2 URL (.net → .info)
- Updated history.dat to 0.130
- Updated catver.ini to 0.130
- Added nplayers.ini

* Wed Jan  7 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0129-1
- Updated mameinfo.dat to 0.129
- Updated history.dat to 0.129
- Updated catver.ini to 0.129

* Sun Oct 19 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0128-1
- Updated mameinfo.dat to 0.128
- Updated history.dat to 0.128
- Updated catver.ini to 0.128
- Switched to the ctrlr files from http://www.kutek.net/mame32_config_files.php

* Wed Aug 20 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0127-1
- Updated mameinfo.dat to 0.127
- Updated history.dat to 0.127
- Updated catver.ini to 0.127
- Dropped cheat.dat until there is a replacement database

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0126-2
- rebuild for buildsys cflags issue

* Fri Jul 11 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0126-1
- Updated mameinfo.dat to 0.126
- Updated history.dat to 0.126
- Updated catver.ini to 0.126
- Updated cheat.dat to 0.123

* Wed Jun 04 2008 Thorsten Leemhuis <belegdol[at]gmail[dot]com> - 0125-2
- rebuild

* Sat May 10 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0125-1
- Updated mameinfo.dat to 0.125
- Updated history.dat to 0.125
- Updated catver.ini to 0.125

* Wed Mar 26 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0124-1
- Updated mameinfo.dat to 0.124
- Updated history.dat to 0.124
- Updated catver.ini to 0.124
- Fixed erroneous version in %%changelog

* Wed Feb  6 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0123-1
- Updated mameinfo.dat to 0.123
- Updated history.dat to 0.123
- Updated catver.ini to 0.123

* Thu Dec 20 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0122-2
- Added catver.ini (#125)
- Fixed mameinfo docs encoding

* Thu Dec 20 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0122-1
- Updated mameinfo.dat to 0.122
- Updated history.dat to 0.122

* Thu Nov 22 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0121-1
- Updated mameinfo.dat to 0.121
- Updated history.dat to 0.121

* Sun Oct 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0120-1
- First attempt at breaking down the package into smaller pieces
- Updated xarcade.cfg
