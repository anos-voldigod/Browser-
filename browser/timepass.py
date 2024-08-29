import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import re

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My own Browser")

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.example.com"))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        back_button = QPushButton('Back')
        back_button.clicked.connect(self.browser.back)

        forward_button = QPushButton('Forward')
        forward_button.clicked.connect(self.browser.forward)

        reload_button = QPushButton('Reload')
        reload_button.clicked.connect(self.browser.reload)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(back_button)
        layout.addWidget(forward_button)
        layout.addWidget(reload_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = self.url_bar.text()
        
        if re.match(r'^(http|https)://', url) or '.' in url:
            if not url.startswith('http'):
                url = 'http://' + url
        else:
            url = f'https://www.google.com/search?q={url}'
        
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

def main():
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
