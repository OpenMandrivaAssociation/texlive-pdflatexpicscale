%global tl_name pdflatexpicscale
%global tl_revision 72650

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.50
Release:	%{tl_revision}.1
Summary:	Support software for downscaling graphics to be included by pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/pdflatexpicscale
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdflatexpicscale.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdflatexpicscale.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pdflatexpicscale.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a script to scale pictures down to a target
resolution before creating a PDF document with pdfLaTeX.

