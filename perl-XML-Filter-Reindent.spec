#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-Reindent
Summary:	XML::Filter::Reindent - reformats whitespace for pretty printing XML
Summary(pl):	XML::Filter::Reindent - przeformatowanie spacji dla ³adnego druku XML-a
Name:		perl-XML-Filter-Reindent
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3283c7e4cf5da68c1ffb17a454f58c6
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Filter-DetectWS
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Filter::Reindent Perl module is a sub class of
XML::Filter::DetectWS.  XML::Filter::Reindent can be used as a PerlSAX
filter to reformat an XML document before sending it to a PerlSAX
handler that prints it (like XML::Handler::Composer).

#%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Filter/Reindent.pm
%{_mandir}/man3/*
