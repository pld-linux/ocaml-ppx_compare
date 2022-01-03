#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Generation of comparison functions from types
Summary(pl.UTF-8):	Generowanie funkcji porównujących z typów
Name:		ocaml-ppx_compare
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_compare/tags
Source0:	https://github.com/janestreet/ppx_compare/archive/v%{version}/ppx_compare-%{version}.tar.gz
# Source0-md5:	13eefa63e5d051dccebdcbdb57ffb962
URL:		https://github.com/janestreet/ppx_compare
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Generation of fast comparison and equality functions from type
expressions and definitions.

This package contains files needed to run bytecode executables using
ppx_compare library.

%description -l pl.UTF-8
Generowanie szybkich funkcji porównujących i przyrównujących z wyrażeń
i definicji typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_compare.

%package devel
Summary:	Generation of comparison functions from types - development part
Summary(pl.UTF-8):	Generowanie funkcji porównujących z typów - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_compare library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_compare.

%prep
%setup -q -n ppx_compare-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_compare/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_compare/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_compare

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_compare
%{_libdir}/ocaml/ppx_compare/META
%{_libdir}/ocaml/ppx_compare/*.cma
%dir %{_libdir}/ocaml/ppx_compare/expander
%{_libdir}/ocaml/ppx_compare/expander/*.cma
%dir %{_libdir}/ocaml/ppx_compare/runtime-lib
%{_libdir}/ocaml/ppx_compare/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_compare/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_compare/expander/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_compare/runtime-lib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_compare/*.cmi
%{_libdir}/ocaml/ppx_compare/*.cmt
%{_libdir}/ocaml/ppx_compare/*.cmti
%{_libdir}/ocaml/ppx_compare/*.mli
%{_libdir}/ocaml/ppx_compare/expander/*.cmi
%{_libdir}/ocaml/ppx_compare/expander/*.cmt
%{_libdir}/ocaml/ppx_compare/expander/*.cmti
%{_libdir}/ocaml/ppx_compare/expander/*.mli
%{_libdir}/ocaml/ppx_compare/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_compare/runtime-lib/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_compare/ppx_compare.a
%{_libdir}/ocaml/ppx_compare/*.cmx
%{_libdir}/ocaml/ppx_compare/*.cmxa
%{_libdir}/ocaml/ppx_compare/expander/ppx_compare_expander.a
%{_libdir}/ocaml/ppx_compare/expander/*.cmx
%{_libdir}/ocaml/ppx_compare/expander/*.cmxa
%{_libdir}/ocaml/ppx_compare/runtime-lib/ppx_compare_lib.a
%{_libdir}/ocaml/ppx_compare/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_compare/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_compare/dune-package
%{_libdir}/ocaml/ppx_compare/opam
