Name:		texlive-pracjourn
Version:	61719
Release:	2
Summary:	Typeset articles for PracTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pracjourn
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pracjourn class is used for typesetting articles in the
PracTeX Journal. It is based on the article class with
modifications to allow for more flexible front-matter and
revision control, among other small changes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pracjourn/pracjourn.cls
%doc %{_texmfdistdir}/doc/latex/pracjourn/README
%doc %{_texmfdistdir}/doc/latex/pracjourn/pjsample.ltx
%doc %{_texmfdistdir}/doc/latex/pracjourn/pjsample.pdf
%doc %{_texmfdistdir}/doc/latex/pracjourn/pracjourn.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pracjourn/pracjourn.dtx
%doc %{_texmfdistdir}/source/latex/pracjourn/pracjourn.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
