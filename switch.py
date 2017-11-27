SWITCH_CASES = {
    1 : [
        'print("This is a makeshift switch statement")',
        'print("It can handle multiple instructions, including ones that need indentation")',
        'for i in range(1, 6):',
        '    print(i)',
        'print("Statements can be written in normal python code, like this one:\\n\\t%s" % "\\n\\t".join(SWITCH_CASES[1]))'],
    'file' : [
        'try:',
        '    with open("file.txt") as f:',
        '        print(f.readline())',
        'except OSError:',
        '    print("File not found")',
        'except IOError:',
        '    print("File not found")',
        'except FileNotFoundError:',
        '    print("File not found")'],
    'default' : ['print("This is the default case")']
    }

def switch(case):
    try:
        exec("\n".join(SWITCH_CASES[case]))
    except KeyError:
        try:
            exec("\n".join(SWITCH_CASES['default']))
        except KeyError:
            print("No default statement")

switch(1)

switch('file')

switch('something')
