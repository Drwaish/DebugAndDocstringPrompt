# Lambda Function 

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
Deploy on AWS Lambda and automate your work.
