import mdutils


class Output:
    def __init__(self, config):
        self.config = config

    def to_markdown(self, doc_annotations):
        mdFile = MdUtils(file_name="test", title="Annotations Test")
        mdFile.create_md_file()
        mdFile.new_header(level=1, title=doc_annotations["Title"])
        mdFile.new_header(level=2, title=doc_annotations["Author"])

        for row in doc_df:
            mdFile.write("*Color:* {}".format(doc_annotations["Highlights"][1]))
            mdFile.write("*Page: * {}".format(doc_annotations["Highlights"][0]))
            mdFile.write(
                "{} {}".format(
                    doc_annotations["Highlights"][1], doc_annotations["Citekey"]
                )
            )
