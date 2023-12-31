# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
async def _clear(patch_project):
    import os

    _dir = 'downloads'

    if os.path.exists(_dir):
        test = [os.remove(os.path.join(patch_project, _dir, x)) for x in os.listdir(_dir)]
