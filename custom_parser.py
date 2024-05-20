
"""

custo parser

class MyArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_help(self, file=None):
        if '-h' in self._option_string_actions or '--help' in self._option_string_actions:
            # Import file2 and parse its arguments
            import file2
            
            # Add file2 arguments to the parser
            file2.parse_args_file2(self)

            # Print combined help strings
            super().print_help(file)
        else:
            super().print_help(file)
"""