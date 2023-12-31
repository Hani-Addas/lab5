'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'Put your API key here'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 
    #set up the post message paramaters
    params = {
        'api_dev_key':API_DEV_KEY,
        'api_option' : 'paste',
        'api_paste_code':body_text,
        'api_paste_name' : title,
        'api_paste_private' : 0 if listed else 1,
        'api_paste_expire_date' : expiration
    }
    #send the post request and get the response
    print('sending POST request to pasteBin')
    resp_msg = requests.post(PASTEBIN_API_POST_URL, date=params)

    #check whether the request was successful 
    if resp_msg.status_code == requests.codes.ok:
        print(f'New paste created: {resp_msg.txt}')
        return resp_msg.text
    else:
        print(f'Request Failed:{resp_msg.txt}')
        print(f'status code:{resp_msg.status_code} ({resp_msg.reason})')

        def main():
            post_new_paste('awsome paste', 'this paste is not useful\ndelete whenever')

        if __name__ == '__main__':
            main()
