# Notes

open pdf
    setup
        quick scan
        Show all Annotation types
        Select annotations to extract
        Assign meanings
    open page
        find first annotation
        extract text
        extract color
        write to yaml/json
        find next annotation
    next page
write to file

doc_contents = dict(
            title=""
            author=""
            year=""
            annotations={Highlight=[], Underline=[], StrikeOut=[]},
        )  # capitalized because that's what is in the PDF data




json contents:

document:
    Title:
    citekey:
    Abstract:
    Highlights:
        Color1:
            text: " "
                page
            text: " "
                page
        Color2:
            text: " "
                page
            text: " "
                page
    Underline:
        Color1:
            text: " "
                page
            text: " "
                page
        Color2:
            text: " "
                page
            text: " "
                page
    StrikeOut:
        Color1:
            text: " "
                page
            text: " "
                page
        Color2:
            text: " "
                page
            text: " "
                page


Master:
    Highlights:
        Color1:
            title:
            citekey:
                text: " "
                    page
                text: " "
                    page
        Color2:
            title:
            citekey:
                text: " "
                    page
                text: " "
                    page

    Underline:
        Color1:
            title:
            citekey:
                text: " "
                    page
                text: " "
                    page
        Color2:
            title:
            citekey:
                text: " "
                    page
                text: " "
                    page

    StrikeOut:
        Color1:
            title:
            citekey:
                text: " "
                    page
                text: " "
                    page
        Color2:
            title:
            citekey:
                text: " "
                    page
                text: " "
                    page