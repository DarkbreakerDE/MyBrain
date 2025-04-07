from text_pipeline.replace_non_breaking import replace_non_breaking
from text_pipeline.concat_too_small_chunks import concat_too_small_chunks
from text_pipeline.remove_control_symbols import remove_control_symbols
from text_pipeline.replace_carriage_returns import replace_carriage_returns
from text_pipeline.remove_line_breaks_dot import remove_line_breaks_dot
from text_pipeline.remove_line_breaks_end_of_string import (
    remove_line_breaks_end_of_string,
)
from text_pipeline.remove_line_breaks_space import remove_line_breaks_space
from text_pipeline.remove_hyphenated_line_break import remove_hyphenated_line_break
from text_pipeline.replace_double_line_breaks import replace_double_line_breaks
from text_pipeline.replace_line_breaks import replace_line_breaks
from pipelines.pipeline import Pipline
from text_pipeline.split_text_spacy import split_text_spacy


def clean(page_text):
    p = Pipline(
        replace_carriage_returns,
        replace_double_line_breaks,
        remove_hyphenated_line_break,
        replace_line_breaks,
        remove_line_breaks_space,
        remove_line_breaks_dot,
        replace_non_breaking,
        split_text_spacy,
        remove_line_breaks_end_of_string,
        remove_control_symbols,
        concat_too_small_chunks,
    )

    r = p.run(page_text)
    return r


# add spaces between 2412341Buchstabe
