%define upstream_name    Term-Size
%define upstream_version 0.207

Name:	 perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release: %mkrel 1

Summary:	Perl extension for retrieving terminal size
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
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

