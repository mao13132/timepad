# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------

class SearchTargetWord:
    @staticmethod
    def search_target_word(msg_text, target_word):

        if target_word == []:
            return False

        if target_word.lower() in msg_text.lower():
            return True
        else:
            return False
