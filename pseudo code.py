# For all users
1. Annotating Tweets

if request.user.is_authenticated:
	goto this url("/")

	while(user_want_to_annotate || all_tweets_are_annotated)
		show_tweet_to_user_for_annotating()
		mark_tweet_as_positive_or_negative()
		if(positive):
			mark_severity_of_tweet()
		goto_next_tweet()
else
	login()


2. See previous annotated tweets

if request.user.is_authenticated:
	goto this url("/tweets/")
	if(responses > 25):
		show_25_responses_per_page_via_in_pagination()
	else:
		user_can_see_all_responses()
else
	login()


3. Need Help?

if request.user.is_authenticated:
	goto this url("/contact/")
	write_issue()
	select_image() # optional
	submit_issue()
else
	login()


# Specifically for Admin

1. Login
if request.user.is_authenticated_as_admin:
	goto this url("/admin")
else:
	login_as_admin()

2. Perform CRUD Operations on Users Email Address
if request.user.is_authenticated_as_admin:
	goto this url("/admin/account/emailaddress/")
else:
	login_as_admin()

3. Perform CRUD Operations on Users
if request.user.is_authenticated_as_admin:
	goto this url("/admin/auth/user/")
else:
	login_as_admin()

4. Perform CRUD Operations on Users Contact Section
if request.user.is_authenticated_as_admin:
	goto this url("/admin/contact/contact/")
else:
	login_as_admin()

5. See all responses of every users
if request.user.is_authenticated_as_admin:
	goto this url("/admin/tweet/response/")
else:
	login_as_admin()

6. To add Tweets
if request.user.is_authenticated_as_admin:
	while(tweets_not_completed()):
		goto this url("/admin/tweet/tweet/add/")
		fill_necessary_details()
		save()
else:
	login_as_admin()

6. Mark Tweet as common for all
if request.user.is_authenticated_as_admin:
	goto this url("admin/tweet/tweet/")
	select_tweets_you_want_to_mark_common_for_all()
	hit_the_action_button_for_mark_common_for_all()
else:
	login_as_admin()

7. Compare Users
if request.user.is_authenticated_as_admin:
	goto this url("compare/")
	select_users_you_want_to_compare()
	calculateKappa() # shown at last
	show_results()
else:
	login_as_admin()


def calculateKappa(request, user1, user2):
    # check if user has view access to view the tweet_response
    if not request.user.has_perm('tweet.view_response'):
        print("User does NOT have view permission to tweet_response")
        content = {
            'description': 'You do not have permission to view tweet_response',
            'message': 'failed',
        }
        return Response(content, status=400)

    # check if both user exists whom we want to compare
    try:
        u1 = User.objects.get(username=user1)
        u2 = User.objects.get(username=user2)
    except ObjectDoesNotExist:
        content = {
            'description': 'Make sure both usernames are correct and both the user exists',
            'message': 'failed',
        }
        return Response(content, status=403)

    # converting users from username to id
    user1 = u1.id
    user2 = u2.id

    # importing neccesary libraries
    import pandas as pd
    from django.db import connection
    from sklearn.metrics import cohen_kappa_score

    # Getting all responses in one query
    query = str(ResponseModel.objects.all().query)

    # Loading all queries in Pandas Dataframe
    df = pd.read_sql_query(query, connection)

    # Removing unwanted Columns
    del df['id']
    del df['priority']

    # Only Keeping Response that are marked as either Positive or Negative
    df = df.drop(df[(df.response == 0) | (df.response == -2)].index)

    # Only keeping reponse of users that we want to compare
    df.loc[df['user_id_id'].isin([user1, user2])]

    # Making 2 dataframe for each user
    df1 = df[df["user_id_id"] == user1]
    df2 = df[df["user_id_id"] == user2]

    # Combining the above 2 different dataframe to same id
    combined_df = pd.merge(df1, df2, on="tweet_id_id")
    if combined_df.empty:
        content = {
            'description': 'No common responses found',
            'message': 'success',
        }
        return Response(content, status=200)

    # Converting Panda Series to List
    tagger1 = combined_df['response_x'].tolist()
    tagger2 = combined_df['response_y'].tolist()
    
    # Calculating Kappa
    cohen_kappa_score = 0
    try:
        cohen_kappa_score = cohen_kappa_score(T1, T2)
        print(cohen_kappa_score)
    except Exception as E:
        print(E)
        cohen_kappa_score = 0
        print(E + "Some exception caught while calculating Kappa Score")

    # Throwing back the results in JSON format
    content = {
        'cohen_kappa_score': cohen_kappa_score,
        'description': 'success',
        'message': 'success',
    }

    return Response(content, status=200)