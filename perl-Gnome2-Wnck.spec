#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Gnome2-Wnck
Summary:	Perl bindings for the Window Navigator Construction Kit library
Summary(pl):	Dowi±zania Perla dla biblioteki Window Navigator Construction Kit
Name:		perl-Gnome2-Wnck
Version:	0.07
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	265bde4a5831a57308580bf0bf94cac5
URL:		http://gtk2-perl.sf.net/
BuildRequires:	libwnck-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.040
BuildRequires:	perl-Gtk2 >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.040
Requires:	perl-Gtk2 >= 1.00
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Wnck module allows a perl developer to use the Window Navigator
Construction Kit library (libwnck for short) to write tasklists and
pagers.

%description -l pl
Modu³ Wnck pozwala programistom perlowym na u¿ywanie biblioteki
Window Navigator Construction Kit (w skrócie libwnck) do tworzenia
list okien i prze³±czników obszarów roboczych.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Wnck/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorarch}/auto/Gnome2/Wnck
%dir %{perl_vendorarch}/Gnome2/Wnck
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Wnck/*.so
%{perl_vendorarch}/auto/Gnome2/Wnck/*.bs
%{perl_vendorarch}/Gnome2/Wnck/Install
%{perl_vendorarch}/Gnome2/*.pm
%{_mandir}/man3/*
