import re

def html_escape(text):
    """Produce entities within text."""
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return "".join(html_escape_table.get(c,c) for c in text)

def month2int(month_str):
    month2num = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7, 
        "august": 8, 
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    if month_str.isdigit():
        return int(month_str)
    else:
        return month2num[month_str.lower()]

def urlify(s):
    # https://stackoverflow.com/questions/1007481/how-to-replace-whitespaces-with-underscore
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)
    return s.lower()

def oxford_comma(l):
    if len(l) <= 2:
        return " and ".join(l)
    else:
        return ", ".join(l[:-1]) + ", and " + l[-1]

def markdown_page(body, **variables):
    def escape_value(value):
        if type(value) == str:
            return f'"{value}"'
        else:
            return value

    header = "\n".join(f'{name}: {escape_value(value)}' for name, value in variables.items())
    return f"---\n{header}\n---\n{body}\n"
