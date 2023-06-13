import difflib

text1 = """
Dear Annabel,
I hope you are doing fine. Are you excited
about the summer break? Thank you for
your last letter. It is always lovely to hear
about what is going on back home.
I am writing to you to invite you to come to
visit me during the holidays. If the
weather is terrible, we could go to the art
and history museums. We could even
spend the day at the park, or walk around
the state fair. We could go to that cafe
you like or take a day trip on the boat.
It would be great to spend a few weeks
with you here in the city. We would have a lot
of fun! I know how much you love the city.
Let me know your thoughts. If you decide
to come, we can start making plans for
what we will do while you are here.
I hope to hear from you soon, and I hope
to see you soon.
With best wishes,
Phillip
"""
 
text1_lines = text1.splitlines()
 
text2 = """
Dear Annabel,
I hope you are doing great. Are you excited
about the winter break? Thank you for
your last letter. It is always lovely to hear
about what is going on back home.
I am writing to you to invite you to come to
visit me during the holidays. If the
weather is terrible, we could go to the art
and history museums. We could even
spend the day at the park, or walk around
the state fair. We could go to that cafe
you like or take a night trip on the boat.
It would be great to spend a few weeks
with you here in the city. We would have a lot
of fun time! I know how much you love the city.
Let me know your thoughts. If you decide
to come, we can start making plans for
what we will do while you are here.
I hope to hear from you soon, and I hope
to see you soon.
With best wishes,
Phillip
"""
 
text2_lines = text2.splitlines()
 
d = difflib.Differ()
diff = list(d.compare(text1_lines, text2_lines))
print ('\n'.join(diff))
