text = '/reverse/<path:text>'
def reverse(text):
    splitext = text.split("/")
    return '/'.join(splitext[::-1])
reverse(text)
print(reverse(text))


