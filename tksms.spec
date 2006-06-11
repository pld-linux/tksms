Summary:	GUI frontend for SMS application. 
Summary(pl):	Interface graficzny do programu SMS.
Name:		tksms
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.ceti.com.pl/~miki/komputery/download/sms/%{name}.tar.gz
# Source0-md5:	8aea73d95931628eb5d6fc38cc71e4f7
URL:		http://www.ceti.com.pl/~miki/komputery/sms.html
Requires:	sms
Requires:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI frontend for SMS application writen in perl and use Tk module.

%description -l pl
GUI frontend do programu SMS napisany w perlu z uzyciem modulu Tk.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ./*sms* $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
