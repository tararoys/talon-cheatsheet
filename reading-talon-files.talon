hello world: 
    ### A basic Talon command is a word or a phrase.
    ""
hello [with an optional phrase] : 
    ### Anything in square braces in a command phrase is optional. 
    ""
howdy*: 
    ### Any word or phrase with a * after it means 'this word or phrase can be said zero or more times in a row"
    ""
hi+: 
    ### Any word or phrase with a + after it means 'this word or phrase can be said one or more times in a row.
    ""
hiya | hola:  
    ### A vertical bar means 'or', as in, you can say 'hiya' or 'hola' to activate this command.
    ""
(hello goodbye) | (hi bye): 
    ### To group phrases together, put parentheses around the words you want to group as a phrase. This means that things like *, + or | will apply to the whole group.
    ""
{user.greetings}: 
    ### If you see a word in curly braces, that means that there is a list of words you can pick off of.  So to trigger this command, find the list user.greetings and pick a word or phrase off of it. 
    ""
<user.salutations>: 
    ### If you see a word in angle brackets, that means it represents a pattern (also known as a 'capture' in Talon).  Patterns are made of all of the above elements, and instead of writing down a really long pattern you write out the pattern in python and give it a useful name.  Of course, in order to speak the command pattern, you have to know the words and phrases that make it up.
    ""
