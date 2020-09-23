# DISCORD-BOT-2
this discord bot is used to manage among us games (mute people at the start of the game and unmute them)
this bot needs permissions to mute and unmute and move people in your discord

**This bot has 4 commands:**  
>1 - **[ ++s ]** to mute everyone who is in your channel  
>2 - **[ ++e ]** to unmute everyone at your channel  
>3 - **[ ++troll 'discord member' ]** this is a troll command: it will move the discord member to every channel in the discord then bring him back to his original channel  
>4 - **[ ++user ]** to get the usernames of all the members that are connected to a channel in your discord to use the troll command on them  

**there is a good feature added to the bot**  
you can use a message on your discord as a way to mute or unmute everyone at your channel  
to do that :  
**you have to get the id of the message and the channel id that has the message, and put them on 'msgID' and 'channel_id' variables that are in (_on_raw_reaction_remove_ and _on_raw_reaction_add_ fonctions in the code)**  

after that:  
**you can mute everyone at your channel just by adding a reaction to this message and unmute them by removing a reaction**
