Name: jo-test
Version: 1.0
Release: 1
Summary: 

License: @@PACKAGE_LICENSE@@
URL: https://github.com/jpmens/jo
Packager: Jess Portnoy <jess@packman.io>


Source0: %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: 
Requires: 

%description



%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
#inspect the Makefile and see if there is a test target, if so then:
#make test


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%_defaultdocdir/%{name} ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
# place license and README files in the right place.
mkdir -p ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
if [ -r LICENSE ];then
	cp LICENSE ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}/
fi

for F in AUTHORS ChangeLog COPYING NEWS INSTALL README*;do
        if [ -r $F ];then
                cp $F ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
        fi
done


%clean
rm -rf %{buildroot}

%pre

%post

%preun

%postun


%files
%defattr(-,root,root,-)
%doc
%_defaultlicensedir/%{name}
%doc %_defaultdocdir/%{name}/*



%changelog
* Mon Jul 4 2016 Jess Portnoy <jess@packman.io> - 1.0-1
- Auto generated by Packman


