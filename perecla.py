#pip install PyQt6 googletrans==4.0.0-rc1
import sys
from PyQt6 import QtWidgets
from googletrans import Translator

# Створюємо додаток
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Перекладач (Google Translate)")
window.setGeometry(200, 200, 600, 400)

translator = Translator()

# Поля для вводу та виводу
input_text = QtWidgets.QTextEdit()
input_text.setPlaceholderText("Введіть текст для перекладу...")

output_text = QtWidgets.QTextEdit()
output_text.setReadOnly(True)
output_text.setPlaceholderText("Тут з'явиться переклад...")

# Вибір мов
from_lang = QtWidgets.QComboBox()
to_lang = QtWidgets.QComboBox()

langs = {
    "auto": "Автовизначення",
    "en": "Англійська",
    "uk": "Українська",
    "ru": "Російська",
    "de": "Німецька",
    "fr": "Французька",
    "es": "Іспанська",
    "pl": "Польська",
}

for code, name in langs.items():
    from_lang.addItem(name, code)
    if code != "auto":
        to_lang.addItem(name, code)

from_lang.setCurrentIndex(0)  # auto
to_lang.setCurrentText("Англійська")

# Кнопка
translate_btn = QtWidgets.QPushButton("Перекласти")

# Функція для перекладу
def translate_text():
    text = input_text.toPlainText().strip()
    if not text:
        output_text.setPlainText("⚠️ Введіть текст для перекладу.")
        return

    src = from_lang.currentData()
    dest = to_lang.currentData()

    try:
        result = translator.translate(text, src=src, dest=dest)
        output_text.setPlainText(result.text)
    except Exception as e:
        output_text.setPlainText(f"Помилка перекладу: {e}")

# Прив'язуємо кнопку
translate_btn.clicked.connect(translate_text)

# Розташування елементів
layout = QtWidgets.QVBoxLayout()
layout.addWidget(QtWidgets.QLabel("Мова оригіналу:"))
layout.addWidget(from_lang)
layout.addWidget(QtWidgets.QLabel("Мова перекладу:"))
layout.addWidget(to_lang)
layout.addWidget(input_text)
layout.addWidget(translate_btn)
layout.addWidget(output_text)

app.setStyleSheet("""
QPushButton 
    {
        background-color: rgb(205, 255, 105);
        font-size: 16px;
        border-style:grown;
        border-width: 10px;
    
    }
QComboBox
    {
        min-width: 200px;
    {
""")



window.setLayout(layout)
window.show()

sys.exit(app.exec())
