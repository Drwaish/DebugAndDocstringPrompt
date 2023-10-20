""" Test deployed lambda from this sript"""
import requests


URL = ''
# Paste code your code here
CODE = '''

'''
# Code Debugger request. Uncomment following code run Debugger Request
request = {
   "body" : {
      "messages" :
       [
            {
            "role": "system",
            "content": '''
                        Your are a very helpful code debbuger.
                        Debug the following code and fix the bugs.
                        '''
            },
            {
            "role": "user",
            "content": CODE
            }
       ]
    }
}
# Docstring Writing request in Numpy Style. Uncomment following code to run  request
# request = {
#     "body": {
#         "messages" :
#         [
#             {
#             "role": "system",
#             "content": '''
#                         Parameters:
#                         ----------           
#                         Return
#                         ------
#                         Consider above to write docstring   of following code in  numpy style,
#                         consider only above two arguments in docstring
#                         and not write 'Notes' and 'Examples' in docstring.'''
#             },
#             {
#             "role": "user",
#             "content": CODE
#             }
#         ]
#    }
# }

# Docstring Writing request in Google Style. Uncomment following code to run  request

# request = {
#     "body": {
#         "messages" :
#         [
#            {
#             "role": "system",
#             "content": "Write docstring of following code in  google style. "
#             },
#             {
#             "role": "user",
#             "content": CODE
#             }
#         ]
#     }
# }

requests.post(URL,json = request, timeout= 5)
