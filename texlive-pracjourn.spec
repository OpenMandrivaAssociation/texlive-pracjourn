%global tl_name pracjourn
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4n
Release:	%{tl_revision}.1
Summary:	Typeset articles for PracTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pracjourn
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pracjourn.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The pracjourn class is used for typesetting articles in the PracTeX
Journal. It is based on the article class with modifications to allow
for more flexible front-matter and revision control, among other small
changes.

