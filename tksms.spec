Summary:	GUI frontend for SMS application
Summary(pl.UTF-8):   Interfejs graficzny do programu SMS
Name:		tksms
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.ceti.com.pl/~miki/komputery/download/sms/%{name}.tar.gz
# Source0-md5:	8aea73d95931628eb5d6fc38cc71e4f7
URL:		http://www.ceti.com.pl/~miki/komputery/sms.html
Requires:	perl-Tk
Requires:	sms
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI frontend for SMS application writen in Perl and using the Tk
module.

%description -l pl.UTF-8
Graficzny interfejs użytkownika do programu SMS napisany w Perlu z
użyciem modułu Tk.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ./*sms* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
