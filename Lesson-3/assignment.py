from PIL import Image, ImageDraw, ImageFont

# 1-2
try:
    a = 1 / 0

except ZeroDivisionError:
    print("Could not divide by zero")

# 3  - yes. the code will run but will not catch any exception

# 4-5 - will catch all exceptions 5 - It's a broad exception handler, and it's not considered best practice. it's
# generally recommended to catch specific exceptions that we anticipate could occur and handle them accordingly,
# rather than catching all exceptions indiscriminately.

#  6 - IOError - catch input/output errors (i.e - file not found). ZeroDivisionError - catch division by zero errors

# 7-10

filename = 'words.txt'
encoding = "utf-8"

# Write name into the file
with open(filename, 'w') as f:
    f.write('Shmulik')

# Read the file content and print it
with open(filename, 'r') as f:
    content = f.read()
print(content)

# Write Hebrew content into the text file
with open(filename, 'a', encoding=encoding) as f:
    f.write('\nמה נשמע?')

# Read the file content and print it
with open(filename, 'r', encoding=encoding) as f:
    content = f.read()
print(content)

# 11
with open('assignment.py', 'r') as f:
    content = f.read()

img = Image.new('RGB', (1200, 1200), color='black')
draw = ImageDraw.Draw(img)

font_path = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
font = ImageFont.truetype(font_path, 22)
draw.text((10, 10), content, font=font, fill='white')

filename = 'assignment.jpg'
img.save(filename)
