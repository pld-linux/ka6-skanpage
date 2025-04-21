#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.0
%define		kframever	6.13.0
%define		qtver		6.8
%define		kaname		skanpage
Summary:	A multi-page scanning application
Name:		ka6-%{kaname}
Version:	25.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e2f99fcd3428b2f1a579e0b04491b1f3
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Pdf-devel >= %{qtver}
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-tools
BuildRequires:	ka6-ksanecore-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kirigami-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kwallet-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-purpose-devel >= %{kframever}
BuildRequires:	kquickimageeditor-devel
BuildRequires:	leptonlib-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	sane-backends-devel
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	tesseract-devel >= 5
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
Conflicts:	kde4-libksane >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skanpage is a multi-page scanning application built using the
KSaneCore library and a QML interface. It supports saving to image and
PDF files. It uses tesseract as an OCR engine.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/skanpage
%{_desktopdir}/org.kde.skanpage.desktop
%{_iconsdir}/hicolor/48x48/apps/skanpage.png
%{_iconsdir}/hicolor/scalable/apps/skanpage.svg
%{_datadir}/metainfo/org.kde.skanpage.appdata.xml
%{_datadir}/qlogging-categories6/skanpage.categories
