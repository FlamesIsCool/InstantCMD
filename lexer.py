from prompt_toolkit.lexers import Lexer
from prompt_toolkit.document import Document
from commands import CMD_COMMANDS


class CMDLexer(Lexer):

    def lex_document(self, document: Document):
        def get_line_tokens(lineno):
            line = document.lines[lineno]
            tokens = self._tokenize(line)
            return tokens

        return get_line_tokens

    def _tokenize(self, line):
        if not line:
            return [("", "")]

        result = []
        parts = self._split_preserving_spaces(line)

        is_first_word = True
        for part in parts:
            if not part:
                continue

            # Whitespace
            if part.isspace():
                result.append(("", part))
                continue

            if is_first_word:
                is_first_word = False
                if part.lower() in CMD_COMMANDS:
                    result.append(("class:command", part))
                else:
                    result.append(("class:text", part))
                continue

            if part in ("|", "||", "&", "&&"):
                result.append(("class:pipe", part))
                is_first_word = True
                continue
            if part.startswith(">") or part.startswith("<") or part in (">>", "2>", "2>>", "1>"):
                result.append(("class:redirect", part))
                continue

            # %VAR%
            if part.startswith("%") and part.endswith("%") and len(part) > 2:
                result.append(("class:variable", part))
                continue

            if (part.startswith('"') and part.endswith('"')) or \
               (part.startswith("'") and part.endswith("'")):
                result.append(("class:string", part))
                continue

            if part.startswith("/") or part.startswith("-"):
                result.append(("class:flag", part))
                continue

            if part.isdigit():
                result.append(("class:number", part))
                continue

            if "\\" in part or "/" in part or ":" in part:
                result.append(("class:path", part))
                continue

            result.append(("", part))

        return result

    def _split_preserving_spaces(self, text):
        tokens = []
        current = ""
        in_space = False

        for char in text:
            is_space = char in (" ", "\t")

            if char in ("|", "&", ">", "<") and not in_space:
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(char)
                continue

            if is_space != in_space:
                if current:
                    tokens.append(current)
                    current = ""
                in_space = is_space

            current += char

        if current:
            tokens.append(current)

        # Merge adjacent operator chars: | | -> ||, > > -> >>, & & -> &&
        merged = []
        i = 0
        while i < len(tokens):
            if i + 1 < len(tokens) and tokens[i] in ("|", "&", ">") and tokens[i] == tokens[i + 1]:
                merged.append(tokens[i] + tokens[i + 1])
                i += 2
            else:
                merged.append(tokens[i])
                i += 1

        return merged
