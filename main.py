import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QPushButton,
    QLabel,
    QFileDialog
)

from analyzer import analyze_resume_and_jd


class CareerBot(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Resume-JD Analysis Chatbot")
        self.resize(800, 700)

        # Store selected files
        self.resume_path = ""
        self.jd_path = ""

        # Main layout
        main_layout = QVBoxLayout()

        # ----------------------------------------
        # HEADER
        # ----------------------------------------

        header = QLabel(
            "🤖 Resume-JD Analysis Chatbot"
        )

        header.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 15px;
        """)

        main_layout.addWidget(header)

        # ----------------------------------------
        # UPLOAD BUTTONS
        # ----------------------------------------

        button_layout = QHBoxLayout()

        self.resume_button = QPushButton(
            "📄 Upload Resume"
        )

        self.jd_button = QPushButton(
            "📋 Upload Job Description"
        )

        self.analyze_button = QPushButton(
            "🔍 Analyze"
        )

        button_layout.addWidget(
            self.resume_button
        )

        button_layout.addWidget(
            self.jd_button
        )

        button_layout.addWidget(
            self.analyze_button
        )

        main_layout.addLayout(
            button_layout
        )

        # ----------------------------------------
        # FILE STATUS
        # ----------------------------------------

        self.status_label = QLabel(
            "Please upload Resume and Job Description."
        )

        self.status_label.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
        """)

        main_layout.addWidget(
            self.status_label
        )

        # ----------------------------------------
        # CHAT AREA
        # ----------------------------------------

        self.chat_area = QTextEdit()

        self.chat_area.setReadOnly(True)

        main_layout.addWidget(
            self.chat_area
        )

        # ----------------------------------------
        # BUTTON CONNECTIONS
        # ----------------------------------------

        self.resume_button.clicked.connect(
            self.upload_resume
        )

        self.jd_button.clicked.connect(
            self.upload_jd
        )

        self.analyze_button.clicked.connect(
            self.analyze_files
        )

        # ----------------------------------------
        # WELCOME MESSAGE
        # ----------------------------------------

        self.bot_message(
            "Hello! 👋\n\n"
            "Upload your Resume and Job Description.\n"
            "Then click Analyze to compare them."
        )

        self.setLayout(main_layout)

    # ========================================
    # BOT MESSAGE
    # ========================================

    def bot_message(self, message):

        self.chat_area.append(
            "🤖 Bot:\n" + message + "\n"
        )

    # ========================================
    # UPLOAD RESUME
    # ========================================

    def upload_resume(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Resume",
            "",
            "Documents (*.pdf *.docx)"
        )

        if file_path:

            self.resume_path = file_path

            self.status_label.setText(
                "Resume selected: " + file_path
            )

            self.bot_message(
                "📄 Resume uploaded successfully!"
            )

    # ========================================
    # UPLOAD JD
    # ========================================

    def upload_jd(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Job Description",
            "",
            "Documents (*.pdf *.docx)"
        )

        if file_path:

            self.jd_path = file_path

            self.status_label.setText(
                "Job Description selected: " + file_path
            )

            self.bot_message(
                "📋 Job Description uploaded successfully!"
            )

    # ========================================
    # ANALYZE
    # ========================================

    def analyze_files(self):

        if not self.resume_path:

            self.bot_message(
                "⚠️ Please upload your Resume first."
            )

            return

        if not self.jd_path:

            self.bot_message(
                "⚠️ Please upload the Job Description first."
            )

            return

        self.bot_message(
            "🔍 Analyzing Resume and Job Description..."
        )

        try:

            result = analyze_resume_and_jd(
                self.resume_path,
                self.jd_path
            )

            self.show_results(result)

        except Exception as error:

            self.bot_message(
                "❌ Error during analysis:\n"
                + str(error)
            )

    # ========================================
    # SHOW RESULTS
    # ========================================

    def show_results(self, result):

        message = ""

        message += "📊 MATCHING SCORE\n"
        message += str(result["score"]) + "%\n\n"

        # Matched skills
        message += "✅ MATCHED SKILLS\n"

        for skill in result["matched_skills"]:
            message += "• " + skill + "\n"

        message += "\n"

        # Missing skills
        message += "❌ MISSING SKILLS\n"

        for skill in result["missing_skills"]:
            message += "• " + skill + "\n"

        message += "\n"

        # Courses
        message += "📚 RECOMMENDED COURSES\n"

        for skill in result["recommendations"]:

            message += "\n" + skill + ":\n"

            for course in result["recommendations"][skill]:
                message += "• " + course + "\n"

        message += "\n"

        # Suggestions
        message += "💡 RESUME SUGGESTIONS\n"

        for suggestion in result["suggestions"]:
            message += "• " + suggestion + "\n"

        message += "\n"

        # Certifications
        message += "🏆 RECOMMENDED CERTIFICATIONS\n"

        for skill in result["certifications"]:

            message += "\n" + skill + ":\n"

            for certification in result["certifications"][skill]:
                message += "• " + certification + "\n"

        self.bot_message(message)


# ========================================
# START APPLICATION
# ========================================

app = QApplication(sys.argv)

window = CareerBot()

window.show()

sys.exit(app.exec())