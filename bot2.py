import discord
from discord.ext import commands, tasks
import random
import os
import urllib
import json
import time
from itertools import cycle
import pymongo
from pymongo import MongoClient
import asyncio
key = "AIzaSyDsOlwpBIcMsCx-MMa_P6PgYMiZfVfE7vU"

id_list = []

is_gotta_live = True
is_pew_live = True
client = commands.Bot(command_prefix = 'mm/')
old_exists = False
old_sub = 0
old_views = 0
games = cycle(['God', 'Nothing cuz im not human idiot', "Rocket League-I'm the rookie bot", "SlaveSim-#freeBottyBot", "Sorry! oh sorry."])

cluster = MongoClient("mongodb+srv://BraveCrayfish97:Rishi135@cluster0-tgpcr.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["BottyBot"]
collection = db["Messages"]
yt_data = db["YT Data"]
#YT DATA ^^^^^^^^^^^^^^^^^^^^^


#Monster Madnes vvvv
boss_alive = False
hp = 0
Cluster = MongoClient("mongodb+srv://BraveCrayfish97:Rishi135@cluster0-4h8af.mongodb.net/MonsterMadness?retryWrites=true&w=majority")
Db = Cluster["MonsterMadness"]
Collection_Plyr_Dmg = Db["PlayerDamageDealt"]
Collection_Plyr_HP = Db["PlayerHP"]
Collection_Servers = Db["Servers"]
#current_time = 0
#end_time = 0
spawn_embed = ""
rarity = ""
link = ""
org_health = 0



@client.event
async def on_ready():
    print("Bot is online")
    
@client.event
async def on_guild_join(guild):
    Db.create_collection(str(guild))
    c = Db[str(guild)]
    post_msg = {"data":"messages", "msgs":0}
    c.insert_one(post_msg)
    post_boss = {"data":"boss", "alive":False, "original_hp":1, "hp":1, "rarity":0, "link":""}
    c.insert_one(post_boss)

    #servers = ""
    #server_ids = ""
    #guilds = await client.fetch_guilds(limit=150).flatten()
    #for guild in guilds:
    #    
    #    servers = servers + str(guild) + ", "
    #    server_ids = server_ids  + (str(guild.id)) + ", "
    #print(servers)
    #rint(server_ids)
    #post = {"names":servers, "ids":server_ids}
    #Collection_Servers.find_one_and_update({},{"$set":post})
    
@client.event
async def on_message(message):
    global boss_alive
    global hp
    global spawn_embed
    global rarity
    global link
    global org_health

    guild = message.guild
    c = Db[str(guild)]
    alive = c.find_one({"data":"boss"})["alive"]

    msg_count = c.find_one({"data":"messages"})["msgs"]
    c.update_one({"data":"messages"}, {"$set":{"msgs":c.find_one({"data":"messages"})["msgs"]+1}})

    if msg_count > 0 and msg_count % 20 == 0:
        if alive == True:
            print(f"There's already a monster alive in {guild}")


        elif alive == False:
            alive = True
            c.update_one({"data":"boss"}, {"$set":{"alive":alive}})
            print("spawning")
            
            rarities = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6]
            rand_num = random.randint(0, 23)
            rarity_num = rarities[rand_num]

            if rarity_num == 1:
                rarity = "LEGENDARY"
                link = "https://images-ext-1.discordapp.net/external/rk7QJuw0uNtKwLlfMMX3RiarmdD37cgfU5wvE9jG4Rc/https/pixeljoint.com/files/icons/full/dragonboss.gif?width=375&height=375"
                #ultra dragon - rly high health ultra hgih dmg
                hp = random.randint(800, 900)
            if rarity_num == 2:
                rarity = "EPIC"
                link = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5d0257a7-3486-47d1-9695-64179c3f1d58/dcynehy-e83e0655-6b56-40b3-8720-5dac5d35ff47.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNWQwMjU3YTctMzQ4Ni00N2QxLTk2OTUtNjQxNzljM2YxZDU4XC9kY3luZWh5LWU4M2UwNjU1LTZiNTYtNDBiMy04NzIwLTVkYWM1ZDM1ZmY0Ny5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.hcAst0hDQv28G7jQEHWDqZ3ePopAL9cbVR0VDtYkxys"
                #giant robot - ultra high health 
                hp = random.randint(900, 1000)
            if rarity_num == 3:
                rarity = "VERY RARE"
                link = "https://i.pinimg.com/originals/a3/5c/e8/a35ce8c6039b3a1a23aca7706e07c6fa.gif"
                #soul skeelton guy
                hp = random.randint(650, 725)
            if rarity_num == 4:
                rarity = "RARE"
                link = "https://i.pinimg.com/originals/5f/ec/3e/5fec3ecbe48174f56fcaeea159a7f0d4.gif"
                #dragon thing ^^^^^^^ high dmg medium health
                hp = random.randint(500, 600)
            if rarity_num == 5:
                rarity = "UNCOMMON"
                link = "https://i.imgur.com/yGHonzD.gif/Amdarais.gif"
                #3 eyed alien ^^^^^
                hp = random.randint(300, 400)
            if rarity_num == 6:
                rarity = "COMMON"
                #dino vvvvv
                link = "https://i.pinimg.com/originals/ab/7f/55/ab7f55f1e7ab1beb5c1f522958343cb4.gif"
                hp = random.randint(250, 350)
                #SkeleWarrior - link = "https://images-ext-2.discordapp.net/external/RwT0OimR3D9RD8yEGcEbN7Agqf8I_6s42javr7aCwCw/https/pixeljoint.com/files/icons/full/skell1.gif"
                
            c.update_one({"data":"boss"}, {"$set":{"hp":hp}})

            c.update_one({"data":"boss"}, {"$set":{"rarity":str(rarity)}})
            c.update_one({"data":"boss"}, {"$set":{"link":link}})

            spawn_embed = await message.channel.send(embed = boss_embed(link = link, rarity = rarity, percent = 100, alive = alive))
            org_health = hp
            c.update_one({"data":"boss"}, {"$set":{"original_hp":org_health}})
    await client.process_commands(message)

@client.command()
async def setdbdefault(ctx):
    guilds = await client.fetch_guilds(limit=150).flatten()
    
    for guild in guilds:
        c = Db[str(guild)]
        post_boss = {"data":"boss", "alive":False, "original_hp":1, "hp":1, "rarity":0, "link":""}
        c.delete_one({"data":"boss"})
        c.insert_one(post_boss)
        post_attack = {"data":"attack", ""}

@client.command()
async def guilddb(ctx):
    guilds = await client.fetch_guilds(limit=150).flatten()
    for guild in guilds:
        c = Db[str(guild)]
        post = {"data":"boss", "alive":False, "original_hp":1, "hp":1, "rarity":0, "link":""}
        c.insert_one(post)
        #Db.create_collection(str(guild))
        print("POG")
##################################################################################################################
#@client.command()
#async def add(ctx, channel_id = "null", *, channel_name = "null"):
#    #id_list.append(channel_id)
#    if channel_name == "null":
#        await ctx.send("Pls specify the **name** of the channel you want to add.\nEx: YT/add (Channel ID Here) Pewdiepie")
#    elif channel_id == "null":
#        await ctx.send("Pls specify the **ID** of the channel you want to add.\nEx: YT/add (Channel ID Here) Mr Beast")
#
#        try:
#            post = {"name":channel_name, "channel_id":channel_id}
#            yt_data.insert_one(post)
#            await ctx.send("Data has been successfully added! :D")
#        except:
#            await ctx.send("Data was **not** added. Pls try again or ask a staff member for help on how to use me!")
##################################################################################################################
@client.command(aliases = ["get data", "data", "stats"])
async def get_data(ctx, *, channel_name):
    nameFound = False
    try:
        url_id = yt_data.find_one({"name":channel_name})["channel_id"]
        nameFound = True
    except Exception as e:
        print(e)
    
    if nameFound == True:
        
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+url_id+"&key=" + key
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        video_count = data['items'][0]["statistics"]["videoCount"]
        sub = data['items'][0]["statistics"]["subscriberCount"]
        total_views = data['items'][0]["statistics"]["viewCount"]
        await ctx.send(f'{channel_name} stats:\nSubscribers: {sub}\nTotal Views: {total_views}\nVideos: {video_count}')
    else:
        await ctx.send("Retry! Channel name: " + channel_name + " was not found. Try adding this channel with its channel id to the database with the 'YT/add'command :(")

@client.command(aliases = ["channels"])
async def all_channels(ctx):
    name_list = []
    try:

        results = yt_data.find({})

        for result in results:
            name_list.append(result["name"])
        await ctx.send(f"Here's a list of all the channels currently stored:\n{name_list}")

    except Exception as e:
        print(e)
        await ctx.send("There are currently no stored channels.")
        
#@client.command(aliases = ["msgs", "total msgs"])
#async def messages(ctx):
#    msg_count = collection.find_one({"name":"total"})["count"]
#    await ctx.send("There have been " + msg_count + " messages since bot was online or message count was set to 0.\nTo reset the message count, use the YT/clear_msg_count command.")
@client.command()
async def ping(ctx):
    await ctx.send(f"Ping is: {round(client.latency * 1000)}ms. This is how long it takes for your input into the controller to reach the servers and execute the input.")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

#@client.command()
#async def on_member_update(before, after):

#************************#
#*******FUN STUFF********#
#************************#

@client.command()
async def troll(ctx, member : discord.Member, game = "Rocket League"):
    if member.display_name == "RXVishi":
        await ctx.send("WHAT THE! HIS TROLLER LEVEL IS OVER 9000! HE'S UNTROLLABLE!!!")
        await ctx.send(f"I'm sorry he's just too strong")
    else:
        await ctx.send(f"{member.mention} Your good at {game}. It was a joke cuz ur not. Get rekt kid.")

@client.command(aliases=['8ball', 'magic'])
async def _8ball(ctx, *, question):

    answers = random.randint(1,8)
    
    if answers == 1:
        out = "It is certain"
    
    elif answers == 2:
        out = "Probably, you could bet 14 dollhairs on it"
    
    elif answers == 3:
        out = "Likely"
    
    elif answers == 4:
        out = "IDK rn. Try asking again."
    
    elif answers == 5:
        out = "Concentrate and ask again"
    
    elif answers == 6:
        out = "I'm not sure the phtotsynthesis of the binary perpendicularity of the DNA in the bisector got blocked on the way to James Charles' left nostril, try again"
    
    elif answers == 7:
        out = "My reply is no for now"
    
    elif answers == 8:
        out = "My sources say that it will likely never happen."

    await ctx.send(f"Question: {question}\nAnswer: {out} Warning! My predictions may change...")

@client.command()
async def when(ctx, user : discord.User):
    mention = user.mention
    date = user.created_at
    await ctx.send(f"{mention} created this account at {date}")

@client.command(aliases = ["msgs"])
async def messages(ctx, person:discord.User = "null"):
    counter = 0
    
    async for message in ctx.channel.history(limit=10000):
        if message.author == person:
            counter += 1
    
    await ctx.send(f"{person.mention} have sent {counter} messages in this text channel's history.")
    
@client.command(aliases = ["delete", "erase"])
async def remove(ctx, *, channel_name = "null"):
    if channel_name == "null":
        await ctx.send("Pls specify the name of the channel you want to remove.\nEx: YT/remove Mr Beast")
    else:
        try:
            yt_data.delete_many({"name":channel_name})
            await ctx.send(f"The data for {channel_name} was successfully deleted.")
        except Exception as e:
            await ctx.send("Deletion was unsuccesful. This was the error message:\n " + e)

@client.command()
async def add(ctx, link = "null", *, name = "null"):
    if name == "null":
        await ctx.send("Pls specify the **name** of the channel you want to add.\nEx: YT/add (Channel ID Here) Pewdiepie")
    
    elif link == "null":
        await ctx.send("Pls specify the **link** of the channel you want to add.\nEx: YT/add (Channel ID Here) Mr Beast")

    else:
        try:
            lst = link.split("/channel/")
            print(lst)
            channel_id = lst[1]
            post = {"name":name, "channel_id":channel_id}
            yt_data.insert_one(post)
            await ctx.send("Data has been successfully added! :D")
        except Exception as e:
            await ctx.send("Data was **not** added. Pls try again or ask a staff member for help on how to use me!")
            print(e)


@client.command()
async def say(ctx, msg):
    await ctx.channel.purge(limit = 1)
    await ctx.send(msg)

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=697516523929206915&permissions=8&scope=bot")
@client.command(aliases = ["boss"])
async def spawn(ctx):
    global boss_alive
    global hp
    global spawn_embed
    global rarity
    global link
    global org_health
    rarities = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    rand_num = random.randint(0, 26)
    rarity_num = rarities[rand_num]
    if rarity_num == 1:
        rarity = "LEGENDARY"
        link = "https://images-ext-1.discordapp.net/external/rk7QJuw0uNtKwLlfMMX3RiarmdD37cgfU5wvE9jG4Rc/https/pixeljoint.com/files/icons/full/dragonboss.gif?width=375&height=375"
        #ultra dragon - rly high health ultra hgih dmg
        hp = random.randint(800, 900)
    if rarity_num == 2:
        rarity = "EPIC"
        link = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5d0257a7-3486-47d1-9695-64179c3f1d58/dcynehy-e83e0655-6b56-40b3-8720-5dac5d35ff47.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNWQwMjU3YTctMzQ4Ni00N2QxLTk2OTUtNjQxNzljM2YxZDU4XC9kY3luZWh5LWU4M2UwNjU1LTZiNTYtNDBiMy04NzIwLTVkYWM1ZDM1ZmY0Ny5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.hcAst0hDQv28G7jQEHWDqZ3ePopAL9cbVR0VDtYkxys"
        #giant robot - ultra high health 
        hp = random.randint(900, 1000)
    if rarity_num == 3:
        rarity = "VERY RARE"
        link = "https://i.pinimg.com/originals/a3/5c/e8/a35ce8c6039b3a1a23aca7706e07c6fa.gif"
        #soul skeelton guy
        hp = random.randint(650, 725)
    if rarity_num == 4:
        rarity = "RARE"
        link = "https://i.pinimg.com/originals/5f/ec/3e/5fec3ecbe48174f56fcaeea159a7f0d4.gif"
        #dragon thing ^^^^^^^ high dmg medium health
        hp = random.randint(500, 600)
    if rarity_num == 5:
        rarity = "UNCOMMON"
    
        
        link = "https://i.imgur.com/yGHonzD.gif/Amdarais.gif"
        #3 eyed alien ^^^^^
        hp = random.randint(300, 400)
        
    if rarity_num == 6:
        rarity = "COMMON"
        #dino vvvvv
        link = "https://i.pinimg.com/originals/ab/7f/55/ab7f55f1e7ab1beb5c1f522958343cb4.gif"
        hp = random.randint(250, 350)
        #SkeleWarrior - link = "https://images-ext-2.discordapp.net/external/RwT0OimR3D9RD8yEGcEbN7Agqf8I_6s42javr7aCwCw/https/pixeljoint.com/files/icons/full/skell1.gif"
    

    if boss_alive == True:
        await ctx.send("There is already a boss alive. Defeat the current boss in order to spawn a new one")
    elif boss_alive == False:
        boss_alive = True
        #await ctx.send("ATTENTION: There is a **EVIL** boss that you must defeat!\nType YT/attack to deal damage to the boss!\nThe more damage you do, the more coins you get! Good Luck!")
        spawn_embed = await ctx.send(embed = boss_embed(ctx, link = link, rarity = rarity, percent = 100))
        org_health = hp
        
@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def attack(ctx):
    global spawn_embed
    global hp
    global boss_alive
    global rarity
    global link
    global org_health
    #global current_time
    #global end_time
    
    #current = time.time()
    guild = ctx.guild
    c = Db[str(guild)]

    alive = c.find_one({"data":"boss"})["alive"]
    hp = c.find_one({"data":"boss"})["hp"]
    rarity = c.find_one({"data":"boss"})["rarity"]
    link = c.find_one({"data":"boss"})["link"]
    org_health = c.find_one({"data":"boss"})["original_hp"]
    critical = random.randint(1, 4)

    if critical == 1:
        
        dmg = random.randint(30, 40)
        
    else:
        dmg = random.randint(8, 12)
        
    hp -= dmg
    c.update_one({"data":"boss"}, {"$set":{"hp":hp}})
    if alive ==  False or hp <= 0:
        await ctx.channel.purge(limit = 1)
        await ctx.send("`The Monster has been slain`")
        alive = False
        c.update_one({"data":"boss"}, {"$set":{"alive":alive}})


    else:
        await ctx.channel.purge(limit = 1)
        await ctx.send(f"{ctx.author.mention}` has dealt {dmg} damage`")
        
        #await ctx.send(f"`The meanie boi has {hp} health left`")
               #end_time = time.time()
        #print(str(current_time) + "\n" + str(end_time)
        post = {"name":str(ctx.author), "damage":dmg}
        Collection_Plyr_Dmg.insert_one(post)

    await spawn_embed.edit(embed = boss_embed(ctx, link = link, rarity = rarity, percent = round(100*hp/org_health), alive=alive))
    
    

#@client.command()
#async 
def boss_embed(ctx = "null", link = "null", rarity = "null", percent = "null", alive = "null"):
    global boss_alive
    
    num_of_bars = round(percent/10)
    health_bar = "█"*num_of_bars + "░"*(10-num_of_bars)


    embed = discord.Embed(

        title = f"Monster has Spawned({rarity})",
        description = "ATTENTION - an EVIL monster has spawned that you must defeat!\n`YT/attack` - deals damage!\nThe more damage you do, the more coins you get! Good Luck!",
        colour = discord.Color.teal()
    )
    embed.set_footer(text = "Tip: Use a bow to deal damage to the boss without getting attacked by it ;)")
    embed.set_image(url = link)
    if alive == True:
        embed.add_field(name = '_ _', value = f"**HEALTH** - **{health_bar}** ({percent}%)", inline = False)

    else:
        embed.add_field(name = '_ _', value = f"**MONSTER HAS BEEN SLAIN**", inline = False)

    embed.set_author(name = "Monster Madness")
    return embed
    #await ctx.send(embed = embed)


@client.command()
async def status(ctx):
    c = Db[str(ctx.guild)]
    alive = c.find_one({"data":"boss"})["alive"]
    await ctx.send(alive)


#@commands.has_permissions(manage_messages = True)

@client.command()
async def kill(ctx):
    global boss_alive
    global hp
    if boss_alive == True:
        boss_alive = False
        hp = 0
        await ctx.send("`The monster has been slain by a heavenly force.`")
    else:
        await ctx.send("`The monster is already dead`")

@client.command()
async def damage(ctx, member : discord.Member = "null"):
    global Collection_Plyr_Dmg
    print(member)
    
    if member == "null":
        print(ctx.author)
        results = Collection_Plyr_Dmg.find({"name":str(ctx.author)})
        total_dmg = 0
        for result in results:
            total_dmg += result["damage"]
        await ctx.send(f"{ctx.author.mention} has dealt a total of {total_dmg} damage to monsters in total")
    else:
        results = Collection_Plyr_Dmg.find({"name":str(member)})
        total_dmg = 0
        for result in results:
            total_dmg += result["damage"]
        await ctx.send(f"{member.mention} has dealt a total of {total_dmg} damage to monsters in total")
    
@client.command()
@commands.has_permissions(manage_messages = True)
async def reset_damage(ctx, member : discord.Member = "null"):
    global Collection_Plyr_Dmg
    if member == "null":
        await ctx.send("`**Please mention a player who's score to reset**`")
    Collection_Plyr_Dmg.delete_many({"name":str(member)})


#def monster_attack(ctx)


@client.command()
async def guildinfo(ctx):
    await ctx.send(f'Name:{ctx.guild}\nID:{ctx.guild.id}')

@client.command()
async def servers(ctx):
    guilds = await client.fetch_guilds(limit=150).flatten()
    for guild in guilds:
        await ctx.send(guild.id)

@attack.error
async def commandname_error(ctx, error):     
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.channel.purge(limit = 1)
            await ctx.send(f"Cool it. You're only allowed to attack once every second")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit = 1)
#@client.event
#async def on_message(message):

#    collection.update_one({"name":"total"},{"$set":{"count":collection.find_one({"name":"total"})["count"]+1}})


client.run('Njk3NTE2NTIzOTI5MjA2OTE1.Xo4bBQ.N9n8ZMVZ8kiHEu1DH0MXgThH0bI')