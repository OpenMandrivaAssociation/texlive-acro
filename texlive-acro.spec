Name:		texlive-acro
Version:	2.9
Release:	1
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
%{_texmfdistdir}/tex/latex/acro
%doc %{_texmfdistdir}/doc/latex/acro

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
