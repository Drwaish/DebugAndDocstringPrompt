# Lambda Function 

# Setup Repo
```bash
git clone https://github.com/Drwaish/DebugAndDocstringPrompt.git
cd DebugAndDocstringPrompt
```
Install dependencies
```
pip install openai
```
Paste openai api key for smooth running of code.


Open Repository in Visual Studio Code.

For locally test lambda function.
```bash
python lambda_function.py
```
For remotely test lambda function.
### Follow following steps
1) Enter url in 'URL' variable
2) Paste your code in 'code' variable
3) Uncomment your request choice

Timeout for POST request is 5 seconds. If Internet connection is slow increase timeout span.
Then 
```bash
python script.py
```
## Debug Function
User hit the lambda function with this payload.
### Payload
```
{ 
   "body" : {
      "messages" :
       [
            {
            "role": "system",
            "content": "Your are a very helpful code debbuger. Debug the following code and fix the bugs."
            },
            {
            "role": "user"
            "content: "'''<Enter your code here>'''"
            }
       ] 
    }
}
```
## Write Docstring 

### Write Docstring in Numpy Style
Payload return  the docstring in google style.
```
{
    "body": {
        "messages" : 
        [
            {
            "role": "system",
            "content": "'Parameters: \\n -------------- \\n Return\\n --------\\n Consider above to write docstring   of following code in  numpy style,  consider only above two arguments in docstring and not write 'Notes' and 'Examples' in docstring."
            },
            {
            "role": "user"
            "content: "'''<Enter your code here>'''"
            }
        ]
   }
}
```

### Write Docstring in Google Style
Payload return  the docstring in google style.
```
{ 
    "body": {
        "messages" :
        [
           {
            "role": "system",
            "content": "Write docstring of following code in  google style. "
            },
            {
            "role": "user",
            "content": "def data():\n return True"
            }
        ]
    }
}
```
# Important Note: 
### Use script.py to test your lambda. 

Deploy on AWS Lambda and automate your work.
