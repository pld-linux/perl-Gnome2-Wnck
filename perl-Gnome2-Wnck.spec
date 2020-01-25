#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pnam	Gnome2-Wnck
Summary:	Perl bindings for the Window Navigator Construction Kit library
Summary(pl.UTF-8):	Dowiązania Perla dla biblioteki Window Navigator Construction Kit
Name:		perl-Gnome2-Wnck
Version:	0.16
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	439f4569ffd7af96ef1d3feaab23760e
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libwnck-devel >= 2.20.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.180
BuildRequires:	perl-Gtk2 >= 1.180
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libwnck >= 2.20.0
Requires:	perl-Glib >= 1.180
Requires:	perl-Gtk2 >= 1.180
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Wnck module allows a perl developer to use the Window Navigator
Construction Kit library (libwnck for short) to write tasklists and
pagers.

%description -l pl.UTF-8
Moduł Wnck pozwala programistom perlowym na używanie biblioteki Window
Navigator Construction Kit (w skrócie libwnck) do tworzenia list okien
i przełączników obszarów roboczych.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Wnck/{*,*/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{perl_vendorarch}/auto/Gnome2/Wnck
%dir %{perl_vendorarch}/Gnome2/Wnck
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Wnck/*.so
%{perl_vendorarch}/Gnome2/Wnck/Install
%{perl_vendorarch}/Gnome2/Wnck.pm
%{_mandir}/man3/Gnome2::Wnck*.3pm*
