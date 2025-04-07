import pypdfium2 as pdfium
from text_pipeline.concat_too_small_chunks import concat_too_small_chunks
from text_pipeline.remove_line_breaks_dot import remove_line_breaks_dot
from text_pipeline.remove_line_breaks_end_of_string import (
    remove_line_breaks_end_of_string,
)
from text_pipeline.remove_line_breaks_space import remove_line_breaks_space
from text_pipeline.remove_hyphenated_line_break import remove_hyphenated_line_break
from text_pipeline.replace_line_breaks import replace_line_breaks
import text_pipeline.concat_sliding_window as sl
import text_pipeline.split_text_spacy as ss
import text_pipeline.pipeline as pipe
from text_pipeline.remove_page_numbers import remove_page_numbers


def foo(folder_name, file_name):

    total_path = folder_name + file_name

    pdf = pdfium.PdfDocument(total_path)

    print(pdf.get_metadata_dict(), "\n")
    for page in pdf:
        print(page.get_textpage().get_text_range())
        break


def sliding_window():
    text = ["A", "B", "C", "D", "E"]  # , "C", "D", "E", "F", "G", "J"

    r = sl.concat_sliding_window(text)

    print(r)


def splitting_sentences():

    text = """Page 2 of 7Dafaalla et al. SpringerPlus (2016) 5:1306
and Greek languages (Robitaille et al. 2011; Shyu et al.
2006; Soares et al. 2012; Mahmud et al. 2004; Wang et al.
2013).
Correct translation and validation of questionnaires
is of paramount importance. The language of question-
naires should be at the level of understanding of the
participants. It is essential to word the questions in a
way that they can easily be understood by participant
and should be according to their educational level and
culture, also we should put in our mind the importance
of understanding the local context, specific issues and
cultural meanings which language carries. If the ques-
tions are interpreted differently by the participants it
will result in wrong answers and responses will thus be
biased (Abdul Momin Kazi 2012). As far as we know, up
to the time of writing this manuscript there is no study
conducted to validate MOS questionnaire in Arabic
lang."""

    r = ss.split_text_spacy(text)

    print(r)


def pipeline():
    text = """Page 2 of 7Dafaalla et al. SpringerPlus (2016) 5:1306
and Greek languages (Robitaille et al. 2011; Shyu et al.
2006; Soares et al. 2012; Mahmud et al. 2004; Wang et al.
2013).
Correct translation and validation of questionnaires
is of paramount importance. The language of question-
naires should be at the level of understanding of the
participants. It is essential to word the questions in a
way that they can easily be understood by participant
and should be according to their educational level and
culture, also we should put in our mind the importance
of understanding the local context, specific issues and
cultural meanings which language carries. If the ques-
tions are interpreted differently by the participants it
will result in wrong answers and responses will thus be
biased (Abdul Momin Kazi 2012). As far as we know, up
to the time of writing this manuscript there is no study
conducted to validate MOS questionnaire in Arabic
lang."""

    p = pipe.Pipline(
        remove_hyphenated_line_break,
        replace_line_breaks,
        remove_line_breaks_space,
        remove_line_breaks_dot,
        ss.split_text_spacy,
        remove_line_breaks_end_of_string,
    )

    r = p.run(text)
    print(r)


def test_concat():
    arr = ["1", "4" * 4, "F" * 50, "5" * 5, "A" * 50, "6" * 6]

    print(concat_too_small_chunks(arr))


def test_page_numbers():

    data = [[""], ["3 4"], ["3 5"], ["6 7"], [""]]

    print(remove_page_numbers(data))
