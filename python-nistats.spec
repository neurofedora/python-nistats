%global modname nistats
%global commit e35dfdff053ed3ca6052a4a58329662ba68ce3b3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        0.1.0
Release:        0.dev.0git%{shortcommit}%{?dist}
Summary:        Modeling and statistical inference on fMRI data in Python

License:        BSD
URL:            https://github.com/nistats/nistats/
Source0:        https://github.com/nistats/nistats/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Nistats is a Python module for fast and easy modeling and statistical analysis
of functional Magnetic Resonance Imaging data.

It leverages the nilearn Python toolbox for neuroimaging data manipulation
(data downloading, visualization, masking).

It is based on developments initiated in the nipy nipy project.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python-setuptools
BuildRequires:  numpy scipy python2-nibabel python2-nilearn python2-pandas
# Test deps
BuildRequires:  python-nose
Requires:       numpy scipy python2-nibabel python2-nilearn python2-pandas

%description -n python2-%{modname}
Nistats is a Python module for fast and easy modeling and statistical analysis
of functional Magnetic Resonance Imaging data.

It leverages the nilearn Python toolbox for neuroimaging data manipulation
(data downloading, visualization, masking).

It is based on developments initiated in the nipy nipy project.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-numpy python3-scipy python3-nibabel python3-nilearn python3-pandas
# Test deps
BuildRequires:  python3-nose
#BuildRequires:  python3-matplotlib
Requires:       python3-numpy python3-scipy python2-nibabel python3-nilearn python3-pandas

%description -n python3-%{modname}
Nistats is a Python module for fast and easy modeling and statistical analysis
of functional Magnetic Resonance Imaging data.

It leverages the nilearn Python toolbox for neuroimaging data manipulation
(data downloading, visualization, masking).

It is based on developments initiated in the nipy nipy project.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE
%doc README.rst examples
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst examples
%{python3_sitelib}/%{modname}*

%changelog
* Tue Nov 03 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.0-0.dev.0gite35dfdf
- Initial package
