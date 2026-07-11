%global tl_name ijmart
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	LaTeX Class for the Israel Journal of Mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ijmart
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ijmart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ijmart.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ijmart.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Israel Journal of Mathematics is published by The Hebrew University
Magnes Press. This class provides LaTeX support for its authors and
editors. It strives to achieve the distinct "look and feel" of the
journal, while having the interface similar to that of the amsart
document class. This will help authors already familiar with amsart to
easily submit manuscripts for The Israel Journal of Mathematics or to
put the preprints in arXiv with minimal changes in the LaTeX source.

