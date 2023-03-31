Name:		texlive-acro
Version:	62925
Release:	2
Summary:	Typeset acronyms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acro
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acro.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
