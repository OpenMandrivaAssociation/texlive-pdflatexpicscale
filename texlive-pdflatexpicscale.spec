Name:		texlive-pdflatexpicscale
Version:	46617
Release:	1
Summary:	Support software for downscaling graphics to be included by pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdflatexpicscale
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdflatexpicscale.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdflatexpicscale.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a script to scale pictures down to a
target resolution before creating a PDF document with pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/pdflatexpicscale
%doc %{_texmfdistdir}/texmf-dist/doc/support/pdflatexpicscale

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
