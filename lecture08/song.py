def void_chorus():
    print("We don't talk about Bruno, no, no, no")
    print("We don't talk about Bruno")

def chorus():
    print(bruno() + ", no, no, no")
    name = bruno()
    print(name)

def param_chorus():
    print(no_talk("Mirabel") + ", no, no, no")
    print(no_talk("Mirabel"))

def bruno():
    return "We don't talk about Bruno"

def no_talk(name):
    return "We don't talk about " + name

def verse1():
    print("It was my wedding day (it was our wedding day)")
    print("We were getting ready, and there "
          "wasn't a cloud in the sky (no clouds allowed in the sky)")
    print("Bruno walks in with a mischievous grin (thunder)")
    print("You telling this story, or am I?")
    print("I'm sorry, mi vida, go on")

def main():
    void_chorus()
    verse1()
    chorus()
    param_chorus()

# after everything has been defined, call the main function
main()