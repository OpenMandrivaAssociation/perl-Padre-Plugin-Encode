%define upstream_name    Padre-Plugin-Encode
%define upstream_version 0.1.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert file to different encoding in Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(Padre)
BuildArch:	noarch

%description
Convert file to different encoding in Padre.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

