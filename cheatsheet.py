from talon import Module, actions, registry
from typing import *
from user.cheatsheet.doc.html import HtmlDoc
from user.cheatsheet.doc.tex import TeXDoc

import os
import re
import sys

mod = Module()

@mod.action_class


class CheatSheetActions:
    def print_small_sheet():
        """print a short version"""
        
        this_dir = os.path.dirname(os.path.realpath(__file__))
        
        doc = HtmlDoc(
            file_path=os.path.join(this_dir, "small_cheatsheet.html"),
                title="Small Talon Cheatsheet",
                css_include_path=os.path.join(this_dir, "style.css"),
            )

        with doc:

            with doc.section(cols=1, css_classes="has-background-link") as sec: 
                sec.context(registry.contexts["user.knausj_talon.modes.wake_up.talon"], context_name="user.knausj_talon.modes.wake_up.talon")
                sec.context(registry.contexts["user.knausj_talon.modes.modes.talon"], context_name="user.knausj_talon.modes.modes.talon")
            
            with doc.section(cols=1, css_classes="talon-contexts has-background-primary") as sec:
                sec.context(registry.contexts["user.knausj_talon.misc.keys.talon"], context_name="user.knausj_talon.misc.keys.talon")
           

            with doc.section(cols=3, css_classes="has-background-primary talon-lists") as sec:
                
                sec.list("user.letter")
                sec.list("user.symbol_key")
                sec.list("user.number_key")
                sec.list("user.modifier_key")
                sec.list("user.arrow_key")
                sec.list("user.special_key")
                sec.capture("user.function_key")
            
            with doc.section(cols=1, css_classes="talon-contexts has-background-warning") as sec:
                sec.context(registry.contexts["user.knausj_talon.modes.dictation_mode.talon"], context_name = "user.knausj_talon.modes.dictation_mode.talon")
                
            with doc.section(cols=3, css_classes= "talon-lists has-background-warning") as sec:
                sec.capture("user.raw_prose")
                sec.list("user.punctuation")
                sec.list("user.prose_snippets")
                sec.capture("user.prose_simple_number")
                sec.capture("user.prose_number_with_dot")
                sec.capture("user.prose_number_with_colon")
                sec.capture("user.formatter_immune")
                sec.list("user.formatters")

            with doc.section(cols=1, css_classes="has-background-danger") as sec:
                sec.context(registry.contexts["user.knausj_talon.mouse_grid.mouse_grid_always.talon"], context_name = "user.knausj_talon.mouse_grid.mouse_grid_always.talon")
                sec.context(registry.contexts["user.knausj_talon.mouse_grid.mouse_grid_open.talon"], context_name = "user.knausj_talon.mouse_grid.mouse_grid_open.talon")  
                sec.context(registry.contexts["user.knausj_talon.misc.mouse.talon"], context_name = "user.knausj_talon.modes.misc.mouse.talon")

            with doc.section(cols=1, css_classes="has-background-success") as sec:
                sec.context(registry.contexts["user.knausj_talon.misc.window_management.talon"], context_name = "user.knausj_talon.misc.window_management.talon")
            
            with doc.section(cols=2, css_classes="has-background-success") as sec:
                sec.list("user.window_snap_positions")

    def print_cheatsheet(format: str):
        """
        Print out a help document of all Talon commands as <format>

        Args:
            format: The format for the help document. Must be 'HTML' or 'TeX'.
        """
        this_dir = os.path.dirname(os.path.realpath(__file__))

        if format.lower() == "html":
            doc = HtmlDoc(
                file_path=os.path.join(this_dir, "cheatsheet.html"),
                title="Giant Talon Command Reference",
                css_include_path=os.path.join(this_dir, "style.css"),
            )

        if format.lower() == "html-dev":
            doc = HtmlDoc(
                file_path=os.path.join(this_dir, "cheatsheet-dev.html"),
                title="Talon Cheatsheet",
                css_href="style.sass",
            )

        if format.lower() == "tex":
            doc = TeXDoc(
                file_path=os.path.join(this_dir, "cheatsheet.tex"),
                title="Talon Cheatsheet",
                preamble_path="preamble.tex",
            )

        with doc:
            with doc.section(cols=2, css_classes="talon-lists") as sec:
#                sec.list(
#                    list_name="user.symbol_key",
#                )
                for talon_list_name, talon_list in registry.lists.items():
                    print("----------------------------------------------------\n")
                    print("length: " + str(len(talon_list[0])))
                    #if len(talon_list[0]) < 100 :
                    if "user" in talon_list_name:
                        sec.list(list_name=talon_list_name)
            with doc.section(cols=2, css_classes="talon-captures") as sec:
#                sec.list(
#                    list_name="user.symbol_key",
#                )
                for talon_capture_name, talon_capture in registry.captures.items():
                    if "user" in talon_capture_name:
                        name = str(talon_capture_name) 
                        sec.capture(capture_name=name)
            with doc.section(cols=2, css_classes="talon-formatters") as sec:
                sec.formatters(
                    list_names=(
                        "user.formatter_code",
                        "user.formatter_prose",
                        "user.formatter_word",
                    ),
                    formatted_text=actions.user.format_text,
                )
            with doc.section(cols=2, css_classes="talon-contexts") as sec:
                for context_name, context in registry.contexts.items():
                    if not "personal" in context_name:
                        sec.context(context, context_name=context_name)
