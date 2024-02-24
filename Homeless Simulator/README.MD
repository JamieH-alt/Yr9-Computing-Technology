# Homeless Simulator Documentation!
## Docs Are Written For An Outdated Version! Currently the game is 2 versions ahead of documentation.
## Version 0.0.1

##### - [Usage](#usage)

## Usage
### Info Pannel
Homeless Simulator's action system is actually quite advanced so far.
It currently will adapt dynamically to the location you are in.

It will give you a little info pannel every time you are ready to run a new action:
E.G. (Infront Restaurant)
```
===============
It's currently 8:00 Oclock!
You are at Infront Restaurant
You can : 
*Move Between Spots
- Infront Restaurant
- Behind Restaurant
*Beg
*Steal
*Fight
*Search
*Inventory
*Exit (Saves!)
What would you like to do? 
```

Now this can be a bit complicated so lets break it down into a few segments.
#### Time
Inside homeless simulator there is a time mechanic.
Currently (As of version 0.0.1) There is no energy mechanic but it will eventually be added.
As such the time is an important part of gameplay.
Every time you do an action the time will go up by atleast ***1 hour***.
This pretty much sums up how the time system works.

#### `Move` and Spots
Inside the game each core location can have many spots.
With the example snippet of the restaurant we have 2 spots.
`Infront Restaurant` and `Behind Restaurant`; To move between these locations 
we can run the command: `move`
Then it will prompt us with:
```
====================================
Where would you like to go? 
```
Which when input with `Infront Restaurant` or `Behind Restaurant` will take us there!
This allows you to travel to spots that have access to actions that are not available at your spot.

#### `Beg`&`Search`
The two commands `Beg` and `Search` both actually do the same thing,
However `Beg` will give you money whereas `Search` can give you money and items!
They will give you a random item which will then get sent to you're inventory!

#### `Inventory`
Inside Homeless Simulator you have an Inventory! It can be accessed with the `Inventory`
command. It shows a little status panel for you're character!
- Here is an Example with items:
```
====================================
You have
*0 Dollars
*10 Health
*24.0 Hunger
These are all the items you have!
*Hotdog
*Cardboard
Would you like to use any items (y or n)? 
```
<p> Now Lets break this down into more digestable parts </p>
<p>The <code>*0 Dollars</code> section of the code shows how much money you have!</p>
<p>The <code>*10 Health</code> Shows you how much health you have, If this reaches 0 you die!</p>
<p>The <code>*24.0 Hunger</code> Shows how hungry you are! Like health if this reaches 0 you will die!</p>
<p></p>
Then it shows us the items the user has with the following code
<blockquote>These are all the items you have!</blockquote>
<blockquote>*Hotdog</blockquote>
<blockquote>*Cardboard</blockquote>
<blockquote>Would you like to use any items (y or n)?</blockquote>

The <code>Hotdog</code> tells us we have a hotdog (which is edible for 1 hunger)
<p></p>
The <code>Cardboard</code> tells us we have a piece of cardboard (which is usable in construction)
<p></p>
The "Would you like to use any items" accepts a "y" or "n"
as an answer.
When answered with a "y" the user picks what item to use.
Structure items like cardboard can be used to create forts.
Forts make sleeping available. The higher tier fort the less hunger
lost when sleeping.