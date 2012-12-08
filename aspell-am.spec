%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.03-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Amharic
%define languagecode am
%define lc_ctype am_ET

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.03.1
Release:       %mkrel 10
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright README* doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.03.1-10mdv2011.0
+ Revision: 662795
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.03.1-9mdv2011.0
+ Revision: 603190
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.03.1-8mdv2010.1
+ Revision: 518904
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.03.1-7mdv2010.0
+ Revision: 413044
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.03.1-6mdv2009.1
+ Revision: 349995
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.03.1-5mdv2009.0
+ Revision: 220359
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.03.1-4mdv2008.1
+ Revision: 182398
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.03.1-3mdv2008.1
+ Revision: 148734
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.03.1-2mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03.1-2mdv2007.0
+ Revision: 123217
- Import aspell-am

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.03.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.03.1-1mdk
- first version

