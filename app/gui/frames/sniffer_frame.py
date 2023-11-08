from queue import Empty

from gui.components import (
    ButtonIcon,
    DetailMessageDialog,
    Frame,
    GroupBox,
    Header,
    VerticalLayout,
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QBoxLayout,
    QPushButton,
    QScrollArea,
)
from network.parsed_message.parsed_message import ParsedMessage

from types_ import ThreadsInfos


class SnifferFrame(Frame):
    def __init__(self, threads_infos: ThreadsInfos, name: str) -> None:
        super().__init__(name)
        self.threads_infos = threads_infos
        self.sniffer_frame_layout = VerticalLayout()
        self.sniffer_frame_layout.setSpacing(0)

        self.set_header_sniffer()
        self.set_list_message()

        self.setLayout(self.sniffer_frame_layout)

        self.timer_check_new_msg = QTimer(self)
        self.timer_check_new_msg.timeout.connect(self.check_new_msg)
        self.timer_check_new_msg.start(300)

    def check_new_msg(self):
        try:
            while True:
                parsed_msg = self.threads_infos["queue_handler_message"].get_nowait()
                self.on_get_message(parsed_msg)
        except Empty:
            pass

    def on_reset(self):
        self.layout_messages.clear_list()

    def on_play(self):
        self.threads_infos["event_play_sniffer"].set()
        self.header_sniffer.do_play(self.threads_infos["event_play_sniffer"].is_set())

    def on_stop(self):
        self.threads_infos["event_play_sniffer"].clear()
        self.header_sniffer.do_play(self.threads_infos["event_play_sniffer"].is_set())

    def set_header_sniffer(self):
        self.header_sniffer = Header()
        self.header_sniffer.setTitle("Sniffeur")

        self.header_sniffer.button_reset = ButtonIcon("restart.svg")
        self.header_sniffer.button_reset.clicked.connect(self.on_reset)
        self.header_sniffer.h_layout.insertWidget(0, self.header_sniffer.button_reset)

        self.header_sniffer.button_play.clicked.connect(self.on_play)
        self.header_sniffer.button_stop.clicked.connect(self.on_stop)
        self.header_sniffer.do_play(self.threads_infos["event_play_sniffer"].is_set())
        self.sniffer_frame_layout.addWidget(self.header_sniffer)

    def set_list_message(self):
        self.box_messages = GroupBox()
        self.box_messages.setTitle("Messages reçus")
        self.box_messages.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_messages = VerticalLayout()
        self.layout_messages.setContentsMargins(0, 0, 0, 0)
        self.layout_messages.addStretch()
        self.layout_messages.setDirection(QBoxLayout.Direction.BottomToTop)
        self.box_messages.setLayout(self.layout_messages)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.box_messages)
        scroll_area.setWidgetResizable(True)

        self.sniffer_frame_layout.addWidget(scroll_area)

    def on_get_message(self, message: ParsedMessage):
        if self.threads_infos.get("event_play_sniffer").is_set():
            button = QPushButton(text=message.__type__)
            button.setFixedHeight(35)
            self.layout_messages.addWidget(button)
            button.clicked.connect(lambda: self.show_info_message_dialog(message))
            if self.layout_messages.count() >= 200:
                self.layout_messages.clear_list(0.1)

    def show_info_message_dialog(self, message):
        dialog = DetailMessageDialog(self, parsed_msg=message)
        dialog.exec()
