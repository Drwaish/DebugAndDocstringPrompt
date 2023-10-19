# Lambda Function 

## Debug Function
User hit the lambda function with this payload.
### Payload
```
{ 
   "body" : 
   {
       "prompt" : """
                Your are a very helpful code debbuger. Debug the following code and fix the bugs.
                "{code}"
                """
   }
}
```
## Write Docstring 

### Write Docstring in Numpy Style
Payload return  the docstring in google style.
```
{
    "body": {
            "numpy_style" : """
                        'Parameters: 
                        -------------- 
                        Return
                        ------'
                         Consider above to write docstring   of following code in  numpy style,  consider only above two arguments in docstring and not write 'Notes' and 'Examples' in docstring.
                         "{code}"
                         """ 
            }
}
```

### Write Docstring in Google Style
Payload return  the docstring in google style.
```
{ 
    "body": {
                "google_style" : """
                         Write docstring of following code in  google style.
                         "{code}"
                         """   
            }   
}
```
Deploy on AWS Lambda and automate your work.
