%define upstream_name    Crypt-OpenSSL-Guess
%define upstream_version 0.11

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Guess OpenSSL include path
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::More)
BuildArch: noarch

%description
Crypt::OpenSSL::Guess provides helpers to guess OpenSSL include path on any
platforms.

Often MacOS's homebrew OpenSSL cause a problem on installation due to
include path is not added. Some CPAN module provides to modify include path
with configure-args, but the Carton manpage or the Module::CPANfile manpage
is not supported to pass configure-args to each modules. Crypt::OpenSSL::*
modules should use it on your the Makefile.PL manpage.

This module resolves the include path by the Net::SSLeay manpage's
workaround. Original code is taken from
'inc/Module/Install/PRIVATE/Net/SSLeay.pm' by the Net::SSLeay manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%make_install

%files
%doc Changes LICENSE META.json META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
