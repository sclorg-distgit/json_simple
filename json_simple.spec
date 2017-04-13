%{?scl:%scl_package json_simple}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

Name:           %{?scl_prefix}json_simple
Version:        1.1.1
Release:        13.%{baserelease}%{?dist}
Summary:        Simple Java toolkit for JSON
License:        ASL 2.0
URL:            http://code.google.com/p/json-simple/
BuildArch:      noarch

# svn export http://json-simple.googlecode.com/svn/tags/tag_release_1_1_1/ json-simple-1.1.1
# tar czf json-simple-1.1.1-src-svn.tar.gz json-simple-1.1.1
Source0:        json-simple-1.1.1-src-svn.tar.gz

#https://code.google.com/p/json-simple/issues/detail?id=97
Patch0:         json-simple-hash-java-1.8.patch

BuildRequires:  %{?scl_prefix_maven}maven-local
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:maven-bundle-plugin)

%description
JSON.simple is a simple Java toolkit for JSON. You can use JSON.simple 
to encode or decode JSON text. 
  * Full compliance with JSON specification (RFC4627) and reliable 
  * Provides multiple functionalities such as encode, decode/parse 
    and escape JSON text while keeping the library lightweight 
  * Flexible, simple and easy to use by reusing Map and List interfaces 
  * Supports streaming output of JSON text 
  * Stoppable SAX-like interface for streaming input of JSON text 
  * Heap based parser 
  * High performance (see performance testing) 
  * No dependency on external libraries 
  * Both of the source code and the binary are JDK1.2 compatible 

%package javadoc
Summary:       API documentation for %{pkg_name}

%description javadoc
This package contains %{summary}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n json-simple-%{version}
find . -name '*.jar' -exec rm -f '{}' \;
# All the files have dos line endings, remove them.
find . -type f -exec %{__sed} -i 's/\r//' {} \;

%patch0 -p1

%mvn_file : %{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc AUTHORS.txt ChangeLog.txt LICENSE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Jan 19 2017 Mat Booth <mat.booth@redhat.com> - 1.1.1-13.1
- Auto SCL-ise package for rh-eclipse46 collection

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-13
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-10
- Update to current packaging guidelines
- Resolves: rhbz#1126522

* Tue Jul 22 2014 Steve Traylen <steve.traylen@cern.ch> - 1.1.1-9
- Skip hash tests for now bug #97

* Mon Jul 21 2014 Steve Traylen <steve.traylen@cern.ch> - 1.1.1-8
- BR junit4 -> junit.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.1.1-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 gil cattaneo <puntogil@libero.it> 1.1.1-1
- update to 1.1.1
- Removed gcj bits
- adapt to current guideline
- add sub package javadoc

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 15 2009 Steve Traylen <steve.traylen@cern.ch> - 1.1-2
- Add AUTHORS.txt and README.txt files.

* Tue Sep 8 2009 Steve Traylen <steve.traylen@cern.ch> - 1.1-1
- Initial build.