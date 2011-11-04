# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pracjourn
# catalog-date 2008-11-30 13:31:17 +0100
# catalog-license gpl
# catalog-version 0.4n
Name:		texlive-pracjourn
Version:	0.4n
Release:	1
Summary:	Typeset articles for PracTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pracjourn
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The pracjourn class is used for typesetting articles in the
PracTeX Journal. It is based on the article class with
modifications to allow for more flexible front-matter and
revision control, among other small changes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
