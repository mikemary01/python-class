import lmproof
def proofread(text):
    proofread = improof.load("en")
    correction = proofread.proofread(text)
    print("original: {}".format(text))
    print("correction: {}".format(correction))
proofread("Your Text")    