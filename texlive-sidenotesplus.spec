%global tl_name sidenotesplus
%global tl_revision 74143

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	Place referenced notes, alerts, figures and tables into the document margin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sidenotesplus
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotesplus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotesplus.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sidenotesplus.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Sidenotesplus is a comprehensive package for placing labeled or
referenced notes, temporary alerts, bibliography references, figures and
tables into the margin. Marginals can be either floated or at fixed
positions relative to the text. Twoside symmetry is preserved. For
BibLaTeX users, macros for side references are provided. Three margin
styles are provided. Two-page symmetric layouts either as (i) Ragged
outer with note reverences in the margin separator or (ii) justified
with last line ragged outer. And (iii) a classic look, justified with
last line ragged right and note reference to the left of the note, but
two-page symmetry is lost. The command \sidenote mimics the \footnote
command and provides labelled (numbers, alphabetic, roman) references.
However, un-numbered and custom symbols can also be specified. Temporary
sidealerts are rendered only if the package option alerton is specified.
Alerts are useful as to do reminders during document development.
Furthermore, captions for figures and tables can also be placed into
margin. Also, full width environments for figures, tables and text are
provided. The text environment can be partially widened, suitable if
that extra space for an equation is required.

