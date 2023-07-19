class Config:
    def __init__(self):
        self.settings = dict(
            pdf_file="./tests/test4.pdf",
            md_file=".tests/test.md",
            citekey="smith2023",
            highlight_enable=True,
            underline_enable=False,
            strikeout_enable=False,
            Highlight_color={
                # MacOS Preview default colors
                "fb5b89": "important",  # pink
                "7cc867": "definition",  # green
                "f9cd59": "default",  # yellow
                "c885da": "methodology",  # purple
                "69aff0": "follow_up",  # blue
            },
            Underline_color={"eb2813": "default"},  # red
            StrikeOut_color={"eb2813": "default"},  # red
        )
