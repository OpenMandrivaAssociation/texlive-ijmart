# revision 30958
# category Package
# catalog-ctan /macros/latex/contrib/ijmart
# catalog-date 2013-06-26 19:53:21 +0200
# catalog-license lppl
# catalog-version 1.7
Name:		texlive-ijmart
Version:	1.7
Release:	3
Summary:	LaTeX Class for the Israel Journal of Mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ijmart
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijmart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijmart.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijmart.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Israel Journal of Mathematics is published by The Hebrew
University Magnes Press. This class provides LaTeX support for
its authors and editors. It strives to achieve the distinct
"look and feel" of the journal, while having the interface
similar to that of the amsart document class. This will help
authors already familiar with amsart to easily submit
manuscripts for The Israel Journal of Mathematics or to put the
preprints in arXiv with minimal changes in the LaTeX source.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ijmart/ijmart.bst
%{_texmfdistdir}/tex/latex/ijmart/ijmart.cls
%doc %{_texmfdistdir}/doc/latex/ijmart/Makefile
%doc %{_texmfdistdir}/doc/latex/ijmart/README
%doc %{_texmfdistdir}/doc/latex/ijmart/ijmart.bib
%doc %{_texmfdistdir}/doc/latex/ijmart/ijmart.pdf
%doc %{_texmfdistdir}/doc/latex/ijmart/ijmsample.bib
%doc %{_texmfdistdir}/doc/latex/ijmart/ijmsample.pdf
%doc %{_texmfdistdir}/doc/latex/ijmart/ijmsample.tex
#- source
%doc %{_texmfdistdir}/source/latex/ijmart/ijmart.dtx
%doc %{_texmfdistdir}/source/latex/ijmart/ijmart.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
