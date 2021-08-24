# [Denzven-Graphing-Api-Bot](https://discord.com/oauth2/authorize?client_id=851532461061308438&permissions=117760&scope=bot)
### Welcome! this is [Denzven-Graphing-Api](https://denzven.pythonanywhere.com/)
### [Invite the bot!](https://discord.com/oauth2/authorize?client_id=851532461061308438&permissions=117760&scope=bot)
### 1. About the Bot:

Denzven-Graphing-Api is my first flask project that plots graphs of formulas/Equations using python. i have also made an [Showcase Bot](https://github.com/denzven/Denzven-Graphing-Api-Bot) to show the abilties of the api 

---

### 2. How to Use the Bot?

Using the Bot is as simple as sending >help or a cmd with some params such as the formula, grid, plot_style, x_coord, y_coord (and 15 others use >attr to see em all) and the Bot will return an image of the plotted Graph.

#### Example of a cmd:

\>fgrem x+y grid=1 line_style=ccff00


![Bot Showcase](https://cdn.discordapp.com/attachments/814689404341059584/866261391396438026/unknown.png)

Note:
- Base Cmd:
    - >fgrem
- The Formula:
    - x+y
    > Note that this formula as the proper symbols

    - What can the formula contain?
        - trignometric functions:
        > sin() cos() tan() 
        - powers
        > x**2 = x²
        - Basic BODMAS           
        >   ()=Brackets,   
            /=Divide,   
            *=Mutiply,  
            +=Add,  
            -=Subtract  
        - Misc:
        >   pi=value of the const pi,  
            sqrt()=square root of the value,  
            %=modulos gives the remaider of 
the divsion  
            - eg: 13%3 returns 1
                  15%5 returns 0

and much more

- The Parameters (>attr): 
    - grid=1
    > Grid refers to the presence of smaller grid lines, represent as boolean value with 1 is true, 0 is false

    - line_style=ccff00
    > the cmd add the graphing line to be a hexcolor of #ccff00

 
---

### 3. Limitations of the API

The API has several limitations in its use now, and is slowly getting patched/fixed.

Some known ones:
- Limitations in the formula usage: the formula must equate to zero. Like "x+y" as input will mean the graph of "x+y=0" and it must contain both x and y in the equation.  
- Limitations in usable functions: No Absolute function, Min, Max (yet!)
- Currently, the API uses Python's eval() function to evaluate the equations, this will be replaced in the future for the sake of performance and stability

---
### 4. Contributing to the API & Bot (if you want to add changes/neaten up the code)

- Fork the repository

> [fork the Api](https://github.com/denzven/Denzven-Graphing-Api/fork)  
> [fork the Bot](https://github.com/denzven/Denzven-Graphing-Api-Bot/fork)

- Clone your fork: `git clone https://github.com/denzven/Denzven-Graphing-Api.git` or `git clone https://github.com/denzven/Denzven-Graphing-Api-Bot.git`
- Create your feature branch: `git checkout -b my-new-feature`
- Commit your changes: `git commit -am 'Add some feature'`
- Push to the branch: `git push origin my-new-feature`
- Submit a pull request


### 5. Known Bugs and Issue reporting

- There was a bug by putting exit() or quit() in the formula that would turn off the api.. i have tried my best to patch it

I dont know of any other feel free to add them in!

### 6. About Me

I am a 17 years old wierdo that hops on with tons of hobbies and gets bored easily. Tried out a bunch of stuff like blender3D, voxel art, making discord bots and telegram bots, basic python programs, right now i am making an Graphing API and its wrapper.
you can find more info about me [here](https://denzven.pythonanywhere.com)

Thank you! Hope You can tribute much needed support and enjoy using the api as much i did making it 😁


[![Top.gg widget of GraphingBot](https://top.gg/api/widget/851532461061308438.svg)](https://top.gg/bot/851532461061308438)
