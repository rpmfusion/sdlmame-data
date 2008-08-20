%define vernumber 127

Name:           sdlmame-data
Version:        0%{vernumber}
Release:        1%{?dist}
Summary:        Data files for the SDLMAME package

Group:          Amusements/Games
License:        Distibutable
URL:            http://mamedev.org
Source1:        http://www.arcade-history.com/dats/mamehistory%{vernumber}.zip
Source2:        http://www.mameworld.net/mameinfo/update/Mameinfo%{version}.zip
Source3:        sdlmame-ctrlr.tgz
Source4:        http://www.progettoemma.net/public/cat/catveren.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  p7zip
Requires:       sdlmame >= %{version}

%description
%{summary}.

%prep
%setup -qcT

# extract DAT files
unzip -qa %{SOURCE1} -d .
7za x %{SOURCE2}
7za x Mameinfo%{version}.exe
mv docs mameinfo
unzip -qa %{SOURCE4} -d .

# fix permissions and line endings
chmod 0644 mameinfo/*.txt
chmod 0755 mameinfo
sed -i 's/\r//' mameinfo/*

#fix encoding
for i in mameinfo/*.txt
do
/usr/bin/iconv -f iso8859-1 -t utf-8 $i > $i.conv && /bin/mv -f $i.conv $i;
done 


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mame
install -pm 644 history.dat mameinfo.dat catveren/Catver.ini\
    $RPM_BUILD_ROOT%{_datadir}/mame
install -d $RPM_BUILD_ROOT%{_datadir}/mame/ctrlr
tar --extract --directory $RPM_BUILD_ROOT%{_datadir}/mame/ctrlr \
    --file %{SOURCE3}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc mameinfo
%{_datadir}/mame


%changelog
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
