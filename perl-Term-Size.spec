%define real_name Term-Size

Summary:	Term::Size - Perl extension for retrieving terminal size
Name:		perl-%{real_name}
Version:	0.2
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Term::Size is a Perl module which provides a straightforward way to get
the size of the terminal (or window) on which a script is running.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
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

