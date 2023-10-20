""" driver function of aws lambda"""
import json
from lambda_function import lambda_handler


def main():
    '''
    Request for lambda function.

    Parameters
    ----------
    None

    Return
    ------
    None
    '''
    # code = input("Enter your code. Line seprated by ")
    code = """
            def buggy_binary_search(arr, target):
                left = 0
                right = len(arr) - 1
                
                while left <= right:
                    mid = (left + right) // 2  # Bug 1: Incorrect midpoint calculation
                    if arr[mid] == target:
                        return mid
                    elif arr[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                return -1  # Bug 2: Incorrect return statement

            # Test the buggy binary search
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            target = 7
            result = buggy_binary_search(arr, target)
            if result != -1:
                print(f"Element {target} found at index {result}")
            else:
                print(f"Element {target} not found in the array")
            """
    options = int(input("Enter Option \n 1 for Code Debug \n 2 for Documentation \n ---->"))
    if options==1:
        with open("prompts/debug_prompt.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        messages = data["messages"]
        messages[1]['content'] = code
    elif options==2:
        with open("prompts/documentation.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        doc_style = int(input("Enter Option \n 1 for Google style  \n 2 for Numpy style \n ---->"))
        if doc_style == 1:
            messages = data["messages"]
            messages = messages[0]
            messages[1]["content"] = code
        elif doc_style==2:
            messages = data["messages"]
            messages = messages[0]
            messages[1]["content"] = code
    # new_prompt = prompt + code

    # prompt = prompt_generate(text)
    request =  {
                "prompt" : messages,
                "isBase64Encoded": False
                }

    content = None
    requests = {}
    requests["body"] = json.dumps(request)
    response =lambda_handler(requests, content)
    if "body" in response:
        print(response['body'])
    else:
        print(response)

if __name__ == "__main__":
    main()
