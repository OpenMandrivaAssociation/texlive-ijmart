# revision 20276
# category Package
# catalog-ctan /macros/latex/contrib/ijmart
# catalog-date 2010-10-30 13:33:19 +0200
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-ijmart
Version:	1.6
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The Israel Journal of Mathematics is published by The Hebrew
University Magnes Press. This class provides LaTeX support for
its authors and editors. It strives to achieve the distinct
"look and feel" of the journal, while having the interface
similar to that of the amsart document class. This will help
authors already familiar with amsart to easily submit
manuscripts for The Israel Journal of Mathematics or to put the
preprints in arXiv with minimal changes in the LaTeX source.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
