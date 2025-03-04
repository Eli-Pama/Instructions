# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instructions 1
- instructions 2
- etc
    ''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions " 
                          "or any key to continue")

if want_instructions == "":
    instructions()

print("program continues")


