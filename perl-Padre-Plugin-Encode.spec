%define upstream_name    Padre-Plugin-Encode
Name:		perl-%{upstream_name}
Version:	0.1.3
Release:	6

Summary:	Convert file to different encoding in Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Padre-Plugin-Encode
Source0:	https://cpan.metacpan.org/authors/id/K/KE/KEEDI/Padre-Plugin-Encode-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(Padre)
BuildArch:	noarch

%description
Convert file to different encoding in Padre.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# require GTK display
# make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.1.3-1mdv2010.0
+ Revision: 381346
- adding missing buildrequires:
- import perl-Padre-Plugin-Encode


* Sat May 30 2009 cpan2dist 0.1.3-1mdv
- initial mdv release, generated with cpan2dist

