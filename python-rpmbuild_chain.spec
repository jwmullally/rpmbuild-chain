%global pypi_name rpmbuild_chain

Name:           python-%{pypi_name}
Version:        0.9
Release:        1%{?dist}
Summary:        Build a series of SRPMs with rpmbuild
License:        MIT
URL:            https://github.com/jwmullally/rpmbuild_chain
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  python-setuptools

#BuildRequires:  python-sphinx
 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python2-%{pypi_name}
Summary:        %{summary}
Requires:       python

%description -n python2-%{pypi_name}
%{summary}

#%package -n     python%{python3_pkgversion}-%{pypi_name}
#Summary:        %{summary}
#Requires:       python%{python3_pkgversion}
#
#%description -n python%{python3_pkgversion}-%{pypi_name}
#%{summary}

#%package -n python-%{pypi_name}-doc
#Summary:        %{pypi_name} documentation
#
#%description -n python-%{pypi_name}-doc
#Documentation for %{pypi_name}

%prep
%autosetup

%build
%{__python2} setup.py build
%{__python3} setup.py build
# generate html docs 
#sphinx-build docs html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
#%{__python3} setup.py install --skip-build --root %{buildroot}
#cp %{buildroot}/%{_bindir}/rpmbuild-chain %{buildroot}/%{_bindir}/rpmbuild-chain-3
#ln -sf %{_bindir}/rpmbuild-chain-3 %{buildroot}/%{_bindir}/rpmbuild-chain-%{python3_version}

%{__python2} setup.py install --skip-build --root %{buildroot}
#cp %{buildroot}/%{_bindir}/rpmbuild-chain %{buildroot}/%{_bindir}/rpmbuild-chain-2
#ln -sf %{_bindir}/rpmbuild-chain-2 %{buildroot}/%{_bindir}/rpmbuild-chain-%{python2_version}

%check
%{__python2} setup.py nosetests
%{__python3} setup.py nosetests

%files -n python2-%{pypi_name}
#%doc 
%{_bindir}/rpmbuild-chain
#%{_bindir}/rpmbuild-chain-2
#%{_bindir}/rpmbuild-chain-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

#%files -n python%{python3_pkgversion}-%{pypi_name}
##%doc 
#%{_bindir}/rpmbuild-chain-3
#%{_bindir}/rpmbuild-chain-%{python3_version}
#%{python3_sitelib}/%{pypi_name}
#%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

#%files -n python-%{pypi_name}-doc
#%doc html 

%changelog
