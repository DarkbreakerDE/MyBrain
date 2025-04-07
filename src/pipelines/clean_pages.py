from pipelines.pipeline import Pipline
from text_pipeline.remove_common_substring import remove_common_substring
from text_pipeline.remove_page_numbers import remove_page_numbers


def clean(pages):
    p = Pipline(
        lambda x: remove_common_substring(
            x,
            threshold_n_strings=1,
            threshold_percentage_pages=0.8,
            threshold_min_digits=10,
            threshold_min_len_substring=4,
        ),
        lambda x: remove_page_numbers(x, threshold_n_strings=1),
    )

    r = p.run(pages)
    return r
