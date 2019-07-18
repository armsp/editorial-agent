import re

semicolon_re = ";" 
colon_re = ":"
dash_re = "( — )+|( - )+"

semicolon_test = ["This is a semicolon; yo semicolon."]
colon_test = ["This is a colon: yo colon."]
dash_test = ["I am thinking of re-covering my sofa.", "Charles Dickens was a great nineteenth-century novelist.", "France has a 35-hour working week.", "You may think she is a liar - she isn't.", "She might come to the party - you never know.", "We’re looking for a dog-friendly hotel.", "For sensitive one-on-one meetings, he is rarely alone; another member of the staff is ordinarily present.", "The suspension of the extradition measure by Carrie Lam, the Beijing-backed chief executive of Hong Kong, and her highly unusual apology on Sunday amounted to a humiliating about-face in response to the protests.", "Mr. Trump has denounced abuses by Iran, Cuba and China — adversaries at odds with the United States on many issues — while soft-pedaling the egregious behavior of repressive political favorites like Saudi Arabia, Egypt and even North Korea."]
#-_
#—_

for test in semicolon_test:
    m = re.search(semicolon_re, test)
    print(m.group())

for test in colon_test:
    m = re.search(colon_re, test)
    print(m.group())
    
for test in dash_test:
    m = re.findall(dash_re, test)
    if m:
        print(m)
    else:
        print(None)