Summary:	Advanced MIDI arpeggiator, programmable step sequencer and LFO
Name:		qmidiarp
Version:	0.6.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/qmidiarp/%{name}-%{version}.tar.bz2
# Source0-md5:	f63011900519ed277a4ace95ba19d2ac
URL:		http://qmidiarp.sourceforge.net/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libtool
BuildRequires:	lv2-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoprovfiles        %{_libdir}/lv2

%description
QMidiArp is an advanced MIDI arpeggiator, programmable step sequencer
and LFO for Linux. It can hold any number of arpeggiator, sequencer,
or LFO modules running in parallel.

- Arpeggiator modules produce sequences depending on the notes sent to
  their input port, which is typically connected to a keyboard or
  another sequencer.

- Step sequencer modules allow you to create simple linear, monophonic
  and globally transposable sequences similar to the first analog
  sequencers.

- MIDI LFO modules independently produce MIDI controller data of
  adjustable waveform, time resolution, amplitude and duration.

- A Global Storage Tool can store different setups and switch between
  them at a given time. It allows you to dynamically combine patterns
  and LFO wave forms.

%package lv2
Summary:	QMidiArp (arpeggiator, step sequencer and LFO) LV2 modules
Group:		Applications
Requires:	%{name}-common = %{version}-%{release}

%description lv2
QMidiArp is an advanced MIDI arpeggiator, programmable step sequencer
and LFO for Linux. It can hold any number of arpeggiator, sequencer,
or LFO modules running in parallel.

- Arpeggiator modules produce sequences depending on the notes sent to
  their input port, which is typically connected to a keyboard or
  another sequencer.

- Step sequencer modules allow you to create simple linear, monophonic
  and globally transposable sequences similar to the first analog
  sequencers.

- MIDI LFO modules independently produce MIDI controller data of
  adjustable waveform, time resolution, amplitude and duration.

- A Global Storage Tool can store different setups and switch between
  them at a given time. It allows you to dynamically combine patterns
  and LFO wave forms.

%package common
Summary:	QMidiArp - common files
Group:		Applications

%description common
Common files for QMidiArp standalone application and LV2 modules.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-nsm

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/qmidiarp
%{_desktopdir}/qmidiarp.desktop
%{_iconsdir}/hicolor/scalable/apps/qmidiarp.svg
%{_datadir}/metainfo/qmidiarp.appdata.xml
%{_mandir}/man1/qmidiarp.1*
%lang(de) %{_mandir}/de/man1/qmidiarp.1*
%lang(fr) %{_mandir}/fr/man1/qmidiarp.1*

%files common -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/translations

%files lv2
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/qmidiarp_arp.lv2
%{_libdir}/lv2/qmidiarp_arp.lv2/manifest.ttl
%attr(755,root,root) %{_libdir}/lv2/qmidiarp_arp.lv2/qmidiarp_arp.so
%{_libdir}/lv2/qmidiarp_arp.lv2/qmidiarp_arp.ttl
%attr(755,root,root) %{_libdir}/lv2/qmidiarp_arp.lv2/qmidiarp_arp_ui.so
%{_libdir}/lv2/qmidiarp_arp.lv2/qmidiarp_arp_ui.ttl
%dir %{_libdir}/lv2/qmidiarp_lfo.lv2
%{_libdir}/lv2/qmidiarp_lfo.lv2/manifest.ttl
%attr(755,root,root) %{_libdir}/lv2/qmidiarp_lfo.lv2/qmidiarp_lfo.so
%{_libdir}/lv2/qmidiarp_lfo.lv2/qmidiarp_lfo.ttl
%attr(755,root,root) %{_libdir}/lv2/qmidiarp_lfo.lv2/qmidiarp_lfo_ui.so
%{_libdir}/lv2/qmidiarp_lfo.lv2/qmidiarp_lfo_ui.ttl
%dir %{_libdir}/lv2/qmidiarp_seq.lv2
%{_libdir}/lv2/qmidiarp_seq.lv2/manifest.ttl
%attr(755,root,root) %{_libdir}/lv2/qmidiarp_seq.lv2/qmidiarp_seq.so
%{_libdir}/lv2/qmidiarp_seq.lv2/qmidiarp_seq.ttl
%attr(755,root,root) %{_libdir}/lv2/qmidiarp_seq.lv2/qmidiarp_seq_ui.so
%{_libdir}/lv2/qmidiarp_seq.lv2/qmidiarp_seq_ui.ttl
