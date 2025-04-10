from gui.test_editor import (
    edit_text_external,
    inline_colored_diff,
    remove_red_ansi_blocks,
)
from pipelines.pipeline import Pipline, map_args
from utils.pritty_format_list import parse_pretty_formatted_list
from utils.pritty_print_list import pretty_print_list


def edit(before, after):
    p = Pipline(
        lambda x, y: map_args(pretty_print_list, x, y),
        inline_colored_diff,
        edit_text_external,
        remove_red_ansi_blocks,
        parse_pretty_formatted_list,
    )

    r = p.run(before, after)
    return r
