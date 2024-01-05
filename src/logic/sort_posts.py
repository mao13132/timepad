# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logic.search_target_word import SearchTargetWord


def sort_posts(posts, search_word, BotDB, organization):
    good_posts = []

    for post in posts:

        in_word_from_post = SearchTargetWord.search_target_word(post['text'], search_word)

        if in_word_from_post:

            id_chat = post['chat_id']

            title = post['title']

            date = post['date_post']

            exist = BotDB.exist_message(id_chat, title, date, organization)

            if exist:
                continue

            good_posts.append(post)

    return good_posts
