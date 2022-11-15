#define beta rc
#define snapshot 20200627
%define major 6

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtdatavis3d
Version:	6.4.1
Release:	%{?beta:0.%{beta}.1}%{?snapshot:1.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtdatavis3d-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtdatavis3d-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{major} 3D data visualization module
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt%{major}Core)
BuildRequires:	cmake(Qt%{major}DBus)
BuildRequires:	cmake(Qt%{major}Qml)
BuildRequires:	cmake(Qt%{major}Gui)
BuildRequires:	cmake(Qt%{major}Widgets)
BuildRequires:	cmake(Qt%{major}OpenGL)
BuildRequires:	cmake(Qt%{major}OpenGLWidgets)
BuildRequires:	cmake(Qt%{major}Quick)
BuildRequires:	cmake(Qt%{major}Network)
BuildRequires:	cmake(Qt%{major}QuickTest)
BuildRequires:	cmake(Qt%{major}Test)
BuildRequires:	cmake(Qt%{major}Qml)
BuildRequires:	cmake(Qt%{major}Qml)
BuildRequires:	qt%{major}-cmake
License:	LGPLv3/GPLv3/GPLv2

%description
Qt %{major} 3D data visualization module

%global extra_files_DataVisualizationQml \
%{_qtdir}/qml/QtDataVisualization

%global extra_devel_files_DataVisualizationQml \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6DataVisualizationQmlplugin*.cmake

%qt6libs DataVisualization DataVisualizationQml

%package examples
Summary: Examples for the Qt %{major} Charts module
Group: Development/KDE and Qt

%description examples
Examples for the Qt %{major} Charts module

%files examples
%{_qtdir}/examples/datavisualization

%prep
%autosetup -p1 -n qtdatavis3d%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
