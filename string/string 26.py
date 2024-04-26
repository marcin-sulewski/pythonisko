import textwrap

text = input("Wpisz text: ")

f_text = textwrap.fill(text, width=50)
print(f_text)
