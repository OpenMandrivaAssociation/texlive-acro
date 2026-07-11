%global tl_name acro
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.8
Release:	%{tl_revision}.1
Summary:	Typeset acronyms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/acro
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acro.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the author to create acronyms in a simple way, and
provides means to add them to different 'classes' of acronyms. Lists can
be created of separate acronym classes. The package option 'single'
instructs the package to ignore acronyms that are used only once in the
whole document. As an experimental feature the package also offers the
option 'sort' which automatically sorts the list created by
\printacronyms.

