import requests, time, json, os
def clear():
    kernel = os.name
    match kernel:
        case 'nt':
            os.system('cls')

        case _:
            os.system('clear')

def breaker():
    clear()
    token = input('Token > ')
    uuid = int(input('Locker ID > '))
    gcid = int(input('Group ID > '))

    endpoint = f'https://discord.com/api/v9/channels/{gcid}/recipients/{uuid}'
    headers = {'authorization': token}

    while True:

        request = requests.delete(endpoint, headers=headers)

        match request.status_code:
            case 204:
                input('Group locker has been removed, press enter to exit > ')
                exit()

            case 429:
                response = json.loads(request.text)
                ratelimit = response.get('retry_after')
                print(f'Sleeping for {ratelimit} seconds')
                time.sleep(int(ratelimit))
                continue

            case _:
                print(request.text)
                print(request.status_code)
                input(f'Invalid token or group, press enter to return to retry > ')
                breaker()                    
