#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Mar 31 17:13:09 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_binary_gen_rand import b_binary_gen_rand  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sip
import wform  # embedded python module
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.Sps = Sps = 8
        self.Rb = Rb = 32000
        self.samp_rate = samp_rate = Rb*Sps
        self.run_stop = run_stop = True
        self.rolloff4 = rolloff4 = 0.
        self.rolloff3 = rolloff3 = 0.35
        self.rolloff2 = rolloff2 = 0.5
        self.rolloff1 = rolloff1 = 1.0
        self.ntaps = ntaps = 128

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, 'Datos')
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, 'Espectro')
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, 'Diagrama de Ojo')
        self.top_grid_layout.addWidget(self.pestana)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	ntaps, #size
        	samp_rate, #samp_rate
        	"Wave Forming", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-3, 3)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('RC Filter Poly', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0.disable_legend()

        labels = ['Rect', 'RC, rollof=1', 'RC, rollof=0.5', 'RC, rollof=0.35', 'RRC, rollof=0',
                  '', '', '', '', '']
        widths = [3, 3, 3, 3, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win)
        self.interp_fir_filter_xxx_0_0_0_0_0_0 = filter.interp_fir_filter_fff(Sps, (wform.rcos(Sps,ntaps,rolloff1)))
        self.interp_fir_filter_xxx_0_0_0_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0_0_0 = filter.interp_fir_filter_fff(Sps, (wform.rect(Sps)))
        self.interp_fir_filter_xxx_0_0_0_0_0.declare_sample_delay(0)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_file_sink_0_0_0_0 = blocks.file_sink(gr.sizeof_float*1, '/media/uis-e3t/DATADRIVE1/MisGitHub/Diagrama-de-ojo-Comunicaciones-II/GNU Radio/BW1', False)
        self.blocks_file_sink_0_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_float*1, '/media/uis-e3t/DATADRIVE1/MisGitHub/Diagrama-de-ojo-Comunicaciones-II/GNU Radio/Rect', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.b_binary_gen_rand_0 = b_binary_gen_rand()
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.15, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.b_binary_gen_rand_0, 0), (self.interp_fir_filter_xxx_0_0_0_0_0, 0))
        self.connect((self.b_binary_gen_rand_0, 0), (self.interp_fir_filter_xxx_0_0_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_file_sink_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rb*self.Sps)
        self.interp_fir_filter_xxx_0_0_0_0_0_0.set_taps((wform.rcos(self.Sps,self.ntaps,self.rolloff1)))
        self.interp_fir_filter_xxx_0_0_0_0_0.set_taps((wform.rect(self.Sps)))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate(self.Rb*self.Sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_rolloff4(self):
        return self.rolloff4

    def set_rolloff4(self, rolloff4):
        self.rolloff4 = rolloff4

    def get_rolloff3(self):
        return self.rolloff3

    def set_rolloff3(self, rolloff3):
        self.rolloff3 = rolloff3

    def get_rolloff2(self):
        return self.rolloff2

    def set_rolloff2(self, rolloff2):
        self.rolloff2 = rolloff2

    def get_rolloff1(self):
        return self.rolloff1

    def set_rolloff1(self, rolloff1):
        self.rolloff1 = rolloff1
        self.interp_fir_filter_xxx_0_0_0_0_0_0.set_taps((wform.rcos(self.Sps,self.ntaps,self.rolloff1)))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.interp_fir_filter_xxx_0_0_0_0_0_0.set_taps((wform.rcos(self.Sps,self.ntaps,self.rolloff1)))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
