# SPDX-FileCopyrightText: 2020 Max Reznik <reznikmm@gmail.com>
#
# SPDX-License-Identifier: MIT

%define debug_package %{nil}

Name:       alr
Version:    0.7.1
Release:    git%{?dist}.1
Summary:    Command-line tool from the Alire project
Group:      Development/Libraries
License:    GPL-3
URL:        https://github.com/alire-project/alire
### Direct download is not availeble
Source0:    alr.tar.gz
Source1:    https://github.com/alire-project/alire/releases/download/v0.7.1/alr-0.7.1-bin-linux.zip
Requires:   git
#BuildRequires:   gcc-gnat
#BuildRequires:   fedora-gnat-project-common  >= 3

# gprbuild only available on these:
ExclusiveArch: %GPRbuild_arches

%description
ALIRE: Ada LIbrary REpository

A catalog of ready-to-use Ada/SPARK libraries plus a command-line tool (alr)
to obtain, build, and incorporate them into your own projects. It aims to
fulfill a similar role to Rust’s cargo or OCaml’s opam.

%prep
%setup -q -c -a1

%build
echo No build from sources yet.

%install
rm -rf %{buildroot}/*
install -d %{buildroot}/%{_bindir}
install bin/alr %{buildroot}/%{_bindir}

%post     -p /sbin/ldconfig
%postun   -p /sbin/ldconfig

%files
%doc LICENSE.txt
%{_bindir}/alr

%changelog
* Fri Nov 27 2020 root - 0.7.1-git.1
- rebuilt

* Fri Nov 27 2020 Maxim Reznik <reznikmm@gmail.com> - 0.7.1-bin
- Initial package from a binary package
