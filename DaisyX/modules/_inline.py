# Must Need to Do For Using This Plugin Given Below:- 
# Port DaisyX/pyroplugs/inlinehelper.py and DaisyX/pyroplugs/formatter.py for using this plugin. 
# Also Check Requirements in this repo Requirements Clearly Mentioned The Requirements needed for this plugin. If that requirements is not available at your repo then add it. 
# Also Need Some Additions At Config Yet Not Added. So Wait Few Time tell plugin don't ready completely to work. 

# Extra Plugins Provided By Team Daisy X
# Ported From WilliamButcher Bot. 
# All Credit Goes to WilliamButcherBot

from DaisyX.pyroplugs.inlinehelper import (
    google_search_func, urban_func, translate_func,
    alive_function, webss, shortify, wall_func,
    saavn_func, deezer_func, inline_help_func,
    torrent_func
)
from DaisyX.services.pyrogram import pbot as app
from pyrogram import filters

__MODULE__ = "Inline"
__HELP__ = """
**alive** - __Check Bot's Stats.__
**tr [LANGUAGE_CODE] [QUERY]** - __Translate Text.__
**ud [QUERY]** - __Urban Dictionary Query.__
**google [QUERY]** - __Google Search.__
**webss [URL]** - __Take Screenshot Of A Website.__
**bitly [URL]** - __Shorten A Link.__
**wall [Query]** - __Find Wallpapers.__
**saavn [SONG_NAME]** - __Get Songs From Saavn.__
**deezer [SONG_NAME]** - __Get Songs From Deezer.__
**torrent [QUERY] - __Torrent Search.__"""



@app.on_message(filters.command("inline"))
async def inline_help(_, message):
    await app.send_message(message.chat.id, text=__HELP__)


@app.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.lower()
        answers = []
        if text.strip() == '':
            answerss = await inline_help_func(__HELP__)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=10
            )
            return
        elif text.split()[0] == "alive":
            answerss = await alive_function(answers)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=10
            )
        elif text.split()[0] == "tr":
            lang = text.split()[1]
            tex = text.split(None, 2)[2]
            answerss = await translate_func(answers, lang, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=10
            )
        elif text.split()[0] == "ud":
            tex = text.split(None, 1)[1]
            answerss = await urban_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=10
            )
        elif text.split()[0] == "google":
            tex = text.split(None, 1)[1]
            answerss = await google_search_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=10
            )
        elif text.split()[0] == "webss":
            tex = text.split(None, 1)[1]
            answerss = await webss(tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=2
            )
        elif text.split()[0] == "bitly":
            tex = text.split(None, 1)[1]
            answerss = await shortify(tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=2
            )

        elif text.split()[0] == "wall":
            tex = text.split(None, 1)[1]
            answerss = await wall_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss
            )

        elif text.split()[0] == "saavn":
            tex = text.split(None, 1)[1]
            answerss = await saavn_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss
            )

        elif text.split()[0] == "deezer":
            tex = text.split(None, 1)[1]
            answerss = await deezer_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss
            )

        elif text.split()[0] == "torrent":
            tex = text.split(None, 1)[1]
            answerss = await torrent_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
                cache_time=10
            )

    except (IndexError, TypeError, KeyError, ValueError):
        return
