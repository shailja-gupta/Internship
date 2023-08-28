#!/usr/bin/env python
# coding: utf-8

# In[2]:


import regex as re


# In[3]:


# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
text = 'Python Excercises, PHP excercices.'
print(re.sub('[,. ]', ':', text))


# In[4]:


# Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.
text = 'Earth is a third planet from the sun and the only astronomical object known to harbor life'
list = re.findall('[ae]\w+', text)
print(list)


# In[48]:


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory

pattern = re.compile(r'\b\w{4,}\b')
                     
text = pattern.findall('Earth is a third planet from the sun and the only astronomical object known to harbor life')
print (text)


# In[20]:


# Question 4-Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory

text = 'Earth is a third planet from the sun and the only astronomical object known to harbor life'

pattern = re.compile(r"\b\w{3,5}\b")


print (re.findall(pattern, text))


# In[43]:


# ###Question 5-Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory

string= ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

pattern = re.compile(r" ?\([^)]+\)")

print (re.findall(pattern, string))


# In[42]:


# Question 6-Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression

string =["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for str in string:
    print(re.sub(r" ?\([^])]+\)","", str))


# In[5]:


# Question 7-Write a regular expression in Python to split a string into uppercase letters
text = "ImportanceOfRegularExpresionsInPython"
print(re.findall('[A-Z][^A-Z]*',text))


# In[15]:


# Question 8-Create a function in python to insert spaces between words starting with numbers.


text = "RegularExpression1IsAn2ImportantTopic3InPython"
print(re.sub(r"(\w)([0-9])", r"\1 \2",text))


# In[27]:


#### Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
text= 'RegularExpression1IsAn2ImportantTopic3InPython'
print(re.sub(r"(\w)([A-Z][0-9])",  r"\1 \2",  text))


# In[29]:


# Question 10-Write a python program to extract email address from the text stored in the text file using Regular Expression

text = "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. Please contact us at hr@fliprobo.com for further information"

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)


# In[34]:


# Question 11-Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores
def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'String matched'
    else:
        return ('String not matched')
    
print(text_match('Let us secrifice our today so that our children can have a better tomorrow'))
print(text_match('Python_Progamming_language_1'))
    


# In[39]:


# Question 12- Write a Python program where a string will start with a specific number

def num_match(text):
    patterns = re.compile(r"^5")
    if re.search(patterns, text):
        print ('Yes, Number is matched ')
    else:
        print('No, Number in not matched')
text = input('Enter the Number: ')
num_match(text)

#def match_num(text):
#    text = re.compile(r"^4")
 #   if text.match(text):
 #       return 'Matched Number'
#   else:
 #       return 'Not Matched Number'
#text = input('Enter the number: ')
#match_num(text)
    


# In[6]:


#Question 13- Write a Python program to remove leading zeros from an IP address
ip = '342.06.093.123'
string = re.sub('\.[0]*','.',ip)
print(string)


# In[53]:


#### Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file

f= open(r"C:\Users\SSINFOTECH\Internship Flip Robo\sample.txt", "r")
content = f.read()
pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
dates = re.findall(pattern, content)


# In[48]:


# Question 15- Write a Python program to search some literals strings in a string. 

patterns = ['fox', 'dog', 'horse']
text = 'The quick brown fox jumps over the lazy dog'
for pattern in patterns:
    print('Searching for "%s" in "%s"-', (pattern,text),)
    if re.search(pattern,text):
          print('Matched')
    else:
          print('Not Matched')


# In[110]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "s%" in "%s" from %d to %d', (match.re.pattern, match.string, s, e))


# In[108]:


# Question 17-Write a Python program to find the substrings within a string

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print ('Found "%s"' % match)


# In[112]:


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s=match.start()
    e=match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[118]:


#Question 19-Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

def change_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt )
dt1= "2023-08-24"
print('Old date in YYYY-MM-DD format: ', dt1)
print('New date in DD-MM-YYYY format: ', change_format(dt1))


# In[60]:


#### Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory

text= "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern = re.compile(r"^[0-9]+(\.[0-9]{1,2})")
print(re.findall(pattern, text))                   
                     


# In[120]:


# Question 21- Write a Python program to separate and print the numbers and their position of a given string.
text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999"
for p in re.finditer("\d+", text):
    print(p.group(0))
    print('Index position: ', p.start())


# In[122]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.

text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
num = re.findall('\d+', text)

print('Max_value: ', max(num))


# In[134]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters

text = 'RegularExpressionIsAnImportantTopicInPython'
space = re.sub(r'(\w)([A-Z])', r'\1 \2', text)
print(space)


# In[135]:


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

def text_match(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns,text):
        print ('Yes, Sequence is matched ')
    else:
        print('No, Sequence in not matched')
text = input('Enter the string: ')
text_match(text)
        
    


# In[57]:


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression
#def remove_duplicate(text):
 #   text = "Hello hello world world"
  #  remove_duplicate(text)
#print(re.sub(r'\b(\w+)(\1\b)+', r'\1', text))

def remove_duplicate(text):
    pattern = r'\b(\w+)(?:\W+\1\b)+'
    return re.sub(pattern, r'\1', text, flags=re.IGNORECASE)
text="Hello hello world world"
print(remove_duplicate(text))


# In[58]:


# Question 26- Write a python program using RegEx to accept string ending with alphanumeric character

def check(str):
    pattern = '[a-zA-Z0-9]$'
    if(re.search(pattern, str)):
        return "The string is ending with alphanumeric character"
    else:
        return "The string does not end with alphanumeric character"
str = input("Enter the string: ")
print(check(str))


# In[66]:


# Question 27- Write a python program using RegEx to extract the hashtags

text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern = (re.findall(r"(#\w+)", text))
print(pattern)


# In[76]:


# Question 28-Write a python program using RegEx to remove <U+..> like symbols

def remove_symbols(text):
    pattern = (re.findall(r"<U\+[A-F0-9]{2}>"))
    remove_text = re.sub(pattern,"", text)
    return remove_text
text= '"@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders'
print(remove_symbols(text))
#print(pattern,text)


# In[115]:


# ###Question 29-Write a python program to extract dates from the text stored in the text file

string.txt = ('Ron was born on 12-09-1992 and he was admitted to school 15-12-1999')
file = open("string.txt", 'r')
text = file.read()
match = re.findall(r'(\d+/\d+/\d+)', text)
print(match)


# In[ ]:





# In[ ]:





# In[9]:


# Question 30-Create a function in python to remove all words from a string of length between 2 and 4. The use of the re.compile() method is mandatory

text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly"
pattern = re.compile(r'\W*\b\w{2,4}\b')
print(pattern.sub('', text))


# In[ ]:




