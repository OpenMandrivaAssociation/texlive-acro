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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/acro
%dir %{_datadir}/texmf-dist/tex/latex/acro
%dir %{_datadir}/texmf-dist/doc/latex/acro/examples
%doc %{_datadir}/texmf-dist/doc/latex/acro/README
%doc %{_datadir}/texmf-dist/doc/latex/acro/acro-manual.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/acro-manual.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.acflike.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.acflike.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.basic.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.basic.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-109.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-109.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-111.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-111.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-119.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-119.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-154.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.issue-154.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.possessive.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.possessive.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-505891.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-505891.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-507726.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-507726.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-513623.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-513623.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-515295.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-515295.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-542461.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.texsx-542461.tex
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.units.pdf
%doc %{_datadir}/texmf-dist/doc/latex/acro/examples/acro.example.units.tex
%{_datadir}/texmf-dist/tex/latex/acro/acro-examples.sty
%{_datadir}/texmf-dist/tex/latex/acro/acro.sty
%{_datadir}/texmf-dist/tex/latex/acro/acro2.sty
