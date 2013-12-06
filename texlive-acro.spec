# revision 32071
# category Package
# catalog-ctan /macros/latex/contrib/acro
# catalog-date 2013-11-04 18:58:09 +0100
# catalog-license lppl
# catalog-version 1.4c
Name:		texlive-acro
Version:	1.4c
Release:	5
Summary:	Typeset acronyms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acro.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the author to create acronyms in a simple
way, and provides means to add them to different 'classes' of
acronyms. Lists can be created of separate acronym classes. The
package option 'single' instructs the package to ignore
acronyms that are used only once in the whole document. As an
experimental feature the package also offers the option 'sort'
which automatically sorts the list created by \printacronyms.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/acro/acro.sty
%{_texmfdistdir}/tex/latex/acro/acro0.def
%{_texmfdistdir}/tex/latex/acro/acro1.def
%doc %{_texmfdistdir}/doc/latex/acro/README
%doc %{_texmfdistdir}/doc/latex/acro/acro_en.pdf
%doc %{_texmfdistdir}/doc/latex/acro/acro_en.tex
%doc %{_texmfdistdir}/doc/latex/acro/example_one.tex
%doc %{_texmfdistdir}/doc/latex/acro/example_two.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
