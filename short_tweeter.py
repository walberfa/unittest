class Tweet:

    def tweet(api, message):
        if len(message) > 40:
            message = message.strip("!?")
        if len(message) > 40:
            message = message.replace('ck', 'x')
            message = message.replace('ex', 'x')
        if len(message) > 40:
            message = message.replace('and', '&')
        status = api.PostUpdate(message)
        return status

