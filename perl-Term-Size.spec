%define upstream_name    Term-Size
%define upstream_version 0.207

Name:	 perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension for retrieving terminal size
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}

%description
Term::Size is a Perl module which provides a straightforward way to get
the size of the terminal (or window) on which a script is running.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/*/auto/Term/Size
%{perl_vendorlib}/*/auto/Term/Size/*
%{perl_vendorlib}/*/Term/Size.pm
%{_mandir}/*/*



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.207.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.207.0-2mdv2011.0
+ Revision: 555204
- rebuild for 5.12

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.207.0-1mdv2010.0
+ Revision: 392714
- update to 0.207
- using %%perl_convert_version
- fix license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2-8mdv2009.0
+ Revision: 258510
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2-7mdv2009.0
+ Revision: 246527
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2008.1
+ Revision: 152324
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-4mdv2008.0
+ Revision: 25458
- rebuild

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.2-3mdv2008.0
+ Revision: 23830
- rebuild


* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.2-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- initial Mandriva package

