# code by Matt
import Utils

# building the query string from the post form data


def buildquerydataforfriendshipscreate(formdata):
    querydata = '?'

    if formdata['parameters_screen_name'] != "":
        querydata = querydata + 'screen_name=' + formdata['parameters_screen_name']
    if formdata['parameters_user_id'] != "":
        querydata = querydata + '&user_id=' + formdata['parameters_user_id']

    return Utils.oauth_post('https://api.twitter.com/1.1/friendships/create.json' + querydata)
