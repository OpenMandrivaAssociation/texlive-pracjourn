# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pracjourn
# catalog-date 2008-11-30 13:31:17 +0100
# catalog-license gpl
# catalog-version 0.4n
Name:		texlive-pracjourn
Version:	0.4n
Release:	5
Summary:	Typeset articles for PracTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pracjourn
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4n-2
+ Revision: 755058
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4n-1
+ Revision: 719293
- texlive-pracjourn
- texlive-pracjourn
- texlive-pracjourn
- texlive-pracjourn

