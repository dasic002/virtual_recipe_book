# Chefs on the net
For my fourth portfolio project with Code Institute, I built a full stack application of a digital recipe book using Django's framework.

Chefs on the net caters for the self made chefs that want to move their recipe books to a digital platform where users can collate their recipes for personal use and/or share with other users on our website. Create a community where users can can comment, rate and even personalise the recipes with their own twist. 

Only registered users have access to the recipes shared on the site and the rest of its features, such as creating recipes, submitting comments, ratings and adding recipes to their favourites.

Recipes require approval from the superuser to listing the recipe for general viewing on the site, but comments and ratings can can be approved by the recipe owners.

The home page whilst a user is logged in, will display the library of public recipes available, whilst in "My recipes" page, users can view their own recipes and more easily review comments and ratings on their recipes.


[View the deployed webapp here](https://chefs-on-the-net-08c612a798ef.herokuapp.com/)

[View the Agile project here](https://github.com/users/dasic002/projects/6)

![Responsive design mock-up](docs/images/responsive-design.PNG)

***

## Table of contents
* [UX User Experience](#ux---user-experience)
  * [User stories](#user-stories).
  * [Strategy](#strategy)
  * [Scope](#scope)
  * [Surface](#surface)
  * [Structure](#structure)
  * [Wireframes](#wireframes)
  * [Surface](#surface)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)



***


## UX - User Experience

### User stories
#### New Visitor
- Upon reaching the website I want to understand what the site does
- I want to see some content before registering
- I want to easily navigate the site to register or find social media links
- I want to easily sign up and start using the site

#### Registered User
- I want to login and logout easily
- I want to be able to delete my account
- I want to be able to reset my password should I forget it
- I want to be able to create/edit/delete my recipes
- I want to be able to create/edit/delete my comments on recipes
- I want to be able to create/edit/delete my rating on recipes
- I want to be able to add and remove a recipes from my favourites
- I want to be able to review comments and ratings from other user on my recipes
- I want to be able to easily copy an existing recipe to make my own tweaks to it
- I want to be able to submit new food items for approval should they not exist in the database

#### All Users
- I want to be able to easily navigate the site regardless of display size
- I want to get feedback on actions taken on the website
- I want to be able to contact the site admin
- I want to see recipe details when I click on it
- I want to be advised if a page I navigated to no longer exists and easily return to the site


### Strategy
Start with an MVP and build on desirable features, to create a simple and cool website the users will want to visit time and time again.

### Scope
This Project was created using the Agile methodology. It allowed me to focus on the **MUST HAVE** features before working on the following graded by the [MoSCoW Method](https://en.wikipedia.org/wiki/MoSCoW_method).

These features were planned as User stories in GitHub Issues and displayed using a [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) board template in GitHub Projects.

Each issue expands on the user intent, our Acceptance Criteatia and Tasks to build the feature.

![Kanban board in Project](docs/images/kanban_board.PNG)

__Must have features:__
- CLOSED - [USER STORY: draft recipe](https://github.com/dasic002/virtual_recipe_book/issues/8)
- CLOSED - [USER STORY: Approve recipes to publish](https://github.com/dasic002/virtual_recipe_book/issues/9)
- CLOSED - [USER STORY: View Paginated list of recipes](https://github.com/dasic002/virtual_recipe_book/issues/1)
- CLOSED - [USER STORY: Open Recipe](https://github.com/dasic002/virtual_recipe_book/issues/2)
- CLOSED - [USER STORY: View Comments](https://github.com/dasic002/virtual_recipe_book/issues/22)
- CLOSED - [USER STORY: User Login](https://github.com/dasic002/virtual_recipe_book/issues/4)
- CLOSED - [USER STORY: User logout](https://github.com/dasic002/virtual_recipe_book/issues/5)
- CLOSED - [USER STORY: Account registration](https://github.com/dasic002/virtual_recipe_book/issues/3)
- CLOSED - [USER STORY: Create a recipe](https://github.com/dasic002/virtual_recipe_book/issues/6)
- CLOSED - [USER STORY: Private or Public recipes](https://github.com/dasic002/virtual_recipe_book/issues/7)
- CLOSED - [USER STORY: Update existing recipe ](https://github.com/dasic002/virtual_recipe_book/issues/23)
- CLOSED - [USER STORY: Delete Recipe](https://github.com/dasic002/virtual_recipe_book/issues/24)

__Should have:__
- CLOSED - [USER STORY: Comment on recipe ](https://github.com/dasic002/virtual_recipe_book/issues/13)
- CLOSED - [USER STORY: Modify or delete comment on a recipe](https://github.com/dasic002/virtual_recipe_book/issues/15)
- IN PROGRESS - [USER STORY: Approve comments](https://github.com/dasic002/virtual_recipe_book/issues/14)
- OPEN - [USER STORY: Personalise a Recipe](https://github.com/dasic002/virtual_recipe_book/issues/11)

__Could have:__
- CLOSED - [USER STORY: View rating](https://github.com/dasic002/virtual_recipe_book/issues/17)
- OPEN - [USER STORY: Approve changed published recipes](https://github.com/dasic002/virtual_recipe_book/issues/10)
- OPEN - [USER STORY: Mark recipes as favourites](https://github.com/dasic002/virtual_recipe_book/issues/12)
- OPEN - [USER STORY: Add a rating to a recipe](https://github.com/dasic002/virtual_recipe_book/issues/16)
- OPEN - [USER STORY: Add tags to recipe](https://github.com/dasic002/virtual_recipe_book/issues/18)

__Won't have:__
- OPEN - [USER STORY: Add a recipe to weekly meal planner](https://github.com/dasic002/virtual_recipe_book/issues/19)
- OPEN - [USER STORY: Add a meal planner to grocery list](https://github.com/dasic002/virtual_recipe_book/issues/20)
- OPEN - [USER STORY: Add recipe to grocery list](https://github.com/dasic002/virtual_recipe_book/issues/21)


### Structure
A multi page including Account Management and Blog like pages to navigate and manage Recipes. The page is composed of the following sections:
- **Header** - Contains title of the page.

- **Menu** - Navigation links included in the header, but collapse into the hamburger/bars icon on smaller displays, either are always visible in the header.

- **Home** - The first page any visitor lands on, includes a banner section welcoming the visitor and inviting them to sign up, should the visitor not be logged in. The page includes 3 recipes the anonymous user is free to browse. Once the user is signed up and logged in, the same page turns into the Library of published recipes the user is able to browse. Includes Recipe widgets and Page navigation widget.

  - **Recipe widget** - Reusable section containing image, Clickable Title, description and Clickable Author name.

  - **Page navigation widget** - Reusable section containing the pagination buttons to navigate libraries of recipes.

- **My recipes** - Another Library view for recipes the current user has created. Includes Recipe widgets, Page navigation widget, Add recipe button to link the user to a Create recipe form, Edit and delete buttons within the recipe widget to allow the user to edit the recipe or delete it. Deletion of recipe requires confirmation via a modal before execution.

- **User Library** - Accessible when the user click on the author's username on the recipe widget. It forwards the user to the same view as **My Recipes** filtering with the given Author's recipes, but excludes any Add/Edit/Delete Recipe buttons.

### Wireframes
- [Landing page](docs/wireframes/01_landing_page.jpg)
- [Navbar and footer](docs/wireframes/02_navbar_and_footer.jpg)
- [Login page](docs/wireframes/03_login.jpg)
- [Signup page](docs/wireframes/04_sign_up.jpg)
- [Logout page](docs/wireframes/05_logout.jpg)
- [Recipes library page](docs/wireframes/06_recipes_library.jpg)
- [My recipes page](docs/wireframes/07_my_recipes.jpg)
- [Recipe details page](docs/wireframes/08_recipe_details.jpg)
- [New recipe page](docs/wireframes/09_new_recipe.jpg)

### Surface
#### Colour theme
Considering the theme of Chefs gone digital, was inspired too use a sort of Neon/Cyberpunk colour theme.

![Original colour selection](docs/images/colour-scheme.PNG)

#### Typography
Google Fonts included:
- Roboto
- Lato

#### Icons and images
Recognisable icons sourced from [FontAwesome](https://fontawesome.com/) were used for [edit](https://fontawesome.com/icons/pen-to-square?f=classic&s=solid), [delete](https://fontawesome.com/icons/trash?f=classic&s=solid), [like](https://fontawesome.com/icons/heart?f=classic&s=regular) and [rating](https://fontawesome.com/icons/star?f=classic&s=regular) buttons as well as an accompanying image for the error pages [403](https://fontawesome.com/icons/ban?f=classic&s=solid), [404](https://fontawesome.com/icons/circle-question?f=classic&s=regular), [405](https://fontawesome.com/icons/circle-xmark?f=classic&s=regular) and [500](https://fontawesome.com/icons/link-slash?f=classic&s=solid).

Regarding images, a [placeholder image](static/images/placeholder.png) and a [mascot image](static/images/placeholder.png) was generated using [Adobe Firefly - AI image generating tool](https://www.adobe.com/uk/products/firefly.html) through Adobe Photoshop, all other images are sourced from the original recipes online.
Placeholder consists of a muffin with the sort of cyberpunk colouring, whilst the mascot is intended to be a friendly robot chef caricature.

## Features 

### Existing Features
- __The landing page - Welcome__
  - As viewed by an anonymous user (i.e.: not registered and logged in user) - the landing page will consist of:
    - A simple Welcome section welcoming the visitor and inviting the user to sign up.
      <table>
      <tr><th>Mobile</th><th>Desktop</th></tr>
      <tr><td>
      <img src="docs/images/feat_mobile-welcome.PNG" alt="Welcome section mobile" width="150vw"/>
      </td><td>
      <img src="docs/images/feat_desktop-welcome.PNG" alt="Welcome section desktop" width="750vw"/>
      </td></tr>
      </table>
    - 3 sample recipes the visitor is free to explore, without access to rate, save or comment.
      <table>
      <tr><th>Mobile</th><th>Desktop</th></tr>
      <tr><td>
      <img src="docs/images/feat_mobile-sample-recipes.PNG" alt="Sample recipes section mobile" width="150vw"/>
      </td><td>
      <img src="docs/images/feat_desktop-sample-recipes.PNG" alt="Sample recipes section desktop" width="750vw"/>
      </td></tr>
      </table>
  - As viewed by a logged in user - the landing page turns into the published recipes library displaying all recipes users have chosen to publish including the saved status and average rating of the recipe within the recipe card.
      <table>
      <tr><th>Mobile</th><th>Desktop</th></tr>
      <tr><td>
      <img src="docs/images/feat_mobile-recipe-library.PNG" alt="Published recipe section mobile" width="150vw"/>
      </td><td>
      <img src="docs/images/feat_desktop-recipe-library.PNG" alt="Published recipe section desktop" width="750vw"/>
      </td></tr>
      </table>

- __Navigation Menu__
  - The navigation as standard is set to a relative position and at the top of the page. On narrow displays, the navigational links are collapsed into an expandable hamburger icon menu, otherwise the links are displayed across the top. The Menu includes **Home** and either **Login** and **Sign up** or **Logout** and **My recipes** dependant on user login status. If the link belongs to the current page being viewed, that link is highlighted as active. The virtually white text over the dark background remains contrasting enough and in keeping with the cyberpunk look.
      <table>
      <tr><th>Mobile</th><th>Desktop</th></tr>
      <tr><td>
      <img src="docs/images/feat_mobile-nav-menu.PNG" alt="Nav menu mobile" width="150vw"/>
      </td><td>
      <img src="docs/images/feat_desktop-nav-menu.PNG" alt="Nav menu desktop" width="750vw"/>
      </td></tr>
      </table>
  

<!-- - __How to Play__
  - This section revealed on clicking the "How to play" button in the menu or the "?" icon button on the landing page or player prompts, contains various subsections providing instructions with illustrations on how to play the game of kings.<br>
  ![How To Play pg1 of 10](documentation/Feat-htp1_10.PNG) ![How To Play pg2 of 10](documentation/Feat-htp2_10.PNG) ![How To Play pg3 of 10](documentation/Feat-htp3_10.PNG) 
  - The steps are provided in subsections that are navigated using the left and right arrow buttons at the bottom. Whilst the "X" button returns to the game area, this is so the player can refer to the instructions at any time and easily resume their game.<br>
  ![How To Play navigation](documentation/Feat-htp_nav.PNG) 

- __Credits__
  - Includes mentions to those that taught me the game, a link to the repository and a link to contact via my business (Studio Silva) WhatsApp.<br>
  ![Credits section](documentation/Feat-Credits.PNG)

- __Error 404 Page__
  - A page in keeping with the style of the main page of the site to indicate the visitor has stumbled upon an non-existent URL of our site and to point them back to our homepage.<br>
  ![Error 404 page](documentation/Feat-404page.PNG)

- __Player Prompt__
  The player prompt screen prompts the human player(s) that it is their turn, particularly useful when more than one human is playing on the same device, to help keep the player's hand and picks a secret. The prompt includes a section with last actions taken by each player. The prompt will always include the button "READY" for the player to move on to their next action and the "?" icon button as a shortcut to review the instructions.

  - __Initial prompt__ - At the start of the game or round this section will have an entry of "New Game!" or "New Round!" and any actions by players that have taken their turn. Mostly indicating that the players have had a turn to look at their bottom 2 cards and if any of them have decided knock already. The button "READY" will move the player to see their hand, allow shuffling and reveal the bottom 2 cards when done.<br>
  ![Early player prompt](documentation/Feat-player_prompt.PNG)

  - __Mid round prompt__ - After all players have had a chance to see their bottom 2 cards, the "READY" button brings the player to the table view where they can opt to take the card from the discard stack or draw from the draw stack. Hence, the first difference in the prompt is the addition of "Pick a card!" on the heading. The players' actions should also describe them as the player would view on the table. For example:
      - If a player has picked the top card from the discard stack and used it to swap with another in their hand, the syntax will follow <br>
      __"[playerName]__ took the __[name of card on discard stack]__ for their __[position of card in hand]__ , __[name of card discarded from their hand]"__<br>
      This is useful in gameplay to get an idea of how good the other players are doing and for the intriguing moment the player may have lost a good card from their hand.
      - If a player has drawn a new card and swapped a card in their hand, the syntax becomes <br>
      __"[playerName]__ drew for their __[position of card in hand]__ , __[name of card discarded from their hand]"__<br>
      The difference being that it omits the name of the card drawn as in real life no other player would have visibility of what was picked up.
      - If a player has drawn and discarded a card, presumably because the value was too high.<br>
      __"[playerName]__ drew and discarded __[name of card discarded]"__<br>
  ![Mid Round player prompt](documentation/Feat-player_prompt2.PNG)

  - __Last playing prompt of the round__ - After a player has opted to knock on their cards, all players thereafter will see the prompt with the heading changed to "last card!" and see the text "**KNOCKED!**" added at the end of that player's action. This is to offer the others a chance to have their last turn of the round.<br>
  ![last playing prompt of the round](documentation/Feat-player_prompt3.PNG)

  - __End of round prompt__ - Only visible to the knocking player (if human) or to the next human player. This triggers the scoring of all players' cards and the "READY" button will reveal the table view with the scores, players' cards and outcome of the round or game.<br>
  ![end of round prompt](documentation/Feat-player_prompt4.PNG)

- __Player card hand__
  - __Selecting to shuffle and countdown to reveal__
  After the player has gone through the initial prompt, the game displays the player's card hand as they'd see on the table. The player can opt to shuffle 2 cards at a time on their hand in the hope it may reveal higher values on the bottom 2 cards. On clicking "Done" the cards can no longer be selected and the game counts down to reveal these bottom cards.<br>
  ![before selecting to shuffle](documentation/Feat-card_to_shuffle.PNG) 
  ![selecting cards to shuffle](documentation/Feat-card_to_selected_pair.PNG)
  ![Countdown to reveal](documentation/Feat-card_to_btm_reveal.PNG)
  
  - __Selecting a card to swap with picked__
  After the player as picked a card from either stack on the table and accepted to swap that card with one in their hand, the game reuses the same player card hand display to show the player's hand so the player can select which to swap it with. On selection of the card, the game will reveal the card being discarded and countdown the knocking button before moving on to the next player.<br>
  ![selecting cards to shuffle](documentation/Feat-card_to_swap.PNG)
  
- __Knocking - bell icon button__
Available after the player has viewed their bottom 2 cards or swapped or discarded a card, the button for knocking appears with a 3 seconds countdown to allow the player to lock in their hand if they believe they have the winning hand.<br>
![knock after viewing hand for first time](documentation/Feat-knock_on_start.PNG)
![knock after discarding a card](documentation/Feat-knock_after_pick.PNG)<br>
If no other player has knocked yet, the button is enabled still and the icon will appear in the deep purple and contrast well with the background. After another player has knocked, the button is disabled, the content is shown in grey and the countdown is shortened to 1 second as it the player cannot act any longer on it.<br>
![enabled knocking button](documentation/Feat-Knock_enabled.PNG) 
![disabled knocking button](documentation/Feat-Knock_disabled.PNG)<br>

- __Table view__
  - __To pick a card__ - shown after the player has been prompted to pick up a card, this screen displays the table with the other players above, the stacks to pick from in the middle and the player's hand below. In this view, the stacks section has the deep purple background to indicate to the player that their next action involves making a selection here. Should another player have knocked for their hand, a bell icon will appear next to their name.<br>
  ![picking a card from a stack](documentation/Feat-table-cards-dealt.PNG)
  ![knocking player indicated by icon](documentation/Feat-table_knocked.PNG)
  
  - __End of Round/Game__ - shown after the human player has been prompted with end of round, the same view is displayed, except this time the players' cards are all revealed, scores assigned and in place of the stacks of cards in the middle, the round or game outcome is announced and a button prompting the player to move on to the next round or a new game. Also visible at this stage are icons next to the players' names, the winner of the round or game will have a trophy icon. Should the winner not be the player that knocked the icon "2X" is assigned to the knocking player to indicate their score of this round has been doubled. All other players are assigned an "X" icon.<br>
  ![end of round table](documentation/Feat-end_of_round.PNG)
  ![end of round table, knocking player lost](documentation/Feat-end_of_round_doubled.PNG)
  ![end of game table](documentation/Feat-end_of_game.PNG)

- __Player picked card__
This view is displayed when the player has made a selection of picking the card from either stack. It present the picked card in a larger format and offers a reject and an accept button to make their decision. Accepting the card will display the player's hand to select the position in their hand that they are swapping it with. Should the card be picked from the discard stack, rejecting this card will simply return to the table, whilst picking from the draw stack it will discard the card. This is because the player's turn must always end with discarding a card, be it from the draw stack or from their hand.<br>
![view of picked card](documentation/Feat-picked_card.PNG)

### Features Left to Implement
- A more intuitive game for a single human player would display the game on the table and show the moves the bot players make as you would playing the game in real life. For example, the game depicts the table with the players' cards face down and as a bot makes its moves of drawing a card from the draw stack, a card is animated as being removed from the stack and if swapped it displays that movement too. There it is easier to visualise the game as opposed to having to read the summary of steps between turns where some might find it too disjointed in the gameplay.

- To make the game play as accurate to real life, knocking on viewing of the bottom 2 cards of the player's hand should record time taken by the player from the moment the knock button appears and compare that to whoever has knocked too, whoever was quickest to knock after viewing their cards gets the status. However, this is rare for players to want to knock this early and even more so for more than one player to feel confident enough to knock this early and would only be necessary if the game remains played on one single device.

- The game is made to play as a multiplayer, the initial idea was to make the game playable over the internet with multiple human players joining a table, but was advised by my mentor that this is a feature outside of the scope of JavaScript alone and have not learnt about WebSocket yet.

- The original intent with the BotSkill value, was to mimic a bot player that might have poorer memory for remembering the cards accurately. So 1 - as novice, might be a bot that remembers a particular card as being in another position or have thought it's value was higher and risk losing good cards. Whilst level 3 - expert, might remember the cards it has seen with great accuracy or that it employs a very discerning tactic of wanting for only the best cards to be picked up before "knocking", locking their hand.

- More game interactions. Initially planned to include:
  - the option of having sounds on the game;
  - customisable colour theme of cards artwork and table appearance;
  - Illustrated and/or animated reactions on reveals of the cards swapped out, for instance a good swap could display a thumbs up and a "Nice!" text over the card, whereas a bad swap could momentarily turn the image monochrome and display a message of "Oh no!". -->

<!-- ### Features Left to Implement
These features were not implemented just so I did not get distracted with a feature creep and not deliver on my MVP.

#### __Alphabet checklist__
The official Wordle game includes the whole keyboard in the display, highlighting which letters have not been used, which are non-existing in the word of the day and existing or correctly placed. This helps the player visualise which letters they could use on their next guess much like a checklist of the alphabet. It becomes easier to try sounding out words for the next guess without using the letters the game has rules out. 

__How might we create this?__
We have not recreated this feature, but we could potentially use the empty space to the right of the guesses to print out the alphabet and highlighting what letters are still available to use. This would probably be done as dictionary variable, where the alphabet forms the keys and the values are the same as used for listing out the clues in a guess ('-' for unused/unchecked, 'X' for not in word of the day, 'O' for exist in Word of the day, 'C' is in the correct place of the word of the day).


#### __Hard Mode gameplay__
Wordle includes __Hard Mode__ which tracks letters the player has guessed that exist in the selected word and should the player not use them in the next guess they attempt, wordle will not accept the entry. Should the letter be in the correct place, wordle will only accept words with the correctly guessed letters in the same places. 

For example, should the word of the day be __LIVER__ and:
1) the first guess be __PLATE__, then __L__ and __E__ are indicated as exiting but being in the wrong place, the second guess would need to include both __L__ and __E__, so it could __not__ be something like _NERVE_ or _LOUSY_, but could be _LIKED_ or _LOVER_.
2) Should the second guess in fact be __LIKED__, the letters __L__, __I__ and __E__ will be indicated as correctly guessed and need to be used in the same places for the following guess, something looking like __L I _ E _.__, which could be LIFER, LIMEN, LINEN, LINER, LIVED, LIVER just to name a few. 

The aim of this feature is to avoid the player trying completely different words to find other missing letters without the constraints of considering the words that the word of the day could be with the clues given. For instance, without __Hard Mode__ the player's second guess could be __VIRUS__ (after 1st as __PLATE__), it doesn't include __L__ and __E__ that would have been highlighted from _PLATE_, but does include __V__, __I__ and __R__. 

From those 2 guesses, the player should be able to deduce that the word of the day is __LIVER__ on the third guess. 

__How might we create this?__
If we were to implement this feature, we could store the list output from the evaluation of previous guesses to use in a validation of input and comparing the previously correct guessed letter placement matching that in the new guess. 
For letters existing in the selected word, the function evaluating guesses can output a dictionary of these letters, and the input validation checks that these letters are used in the latest input before it proceeds to evaluating for the game. 


#### __Feedback messages__
Wordle has a feedback word for correctly guessing the word of the day at each attempt. Specifically, the following messages display guessing correctly at:
1) first attempt - __Genius__
2) second attempt - __Magnificent__
3) third attempt - __Impressive__
4) fourth attempt - __Splendid__
5) fifth attempt - __Great__
6) sixth attempt - __Phew__

__How might we create this?__
These messages could have been a constant variable as a list and upon winning the round, the message is composed calling the list item by index. The index would be calculated with the length of the list of guesses made minus 1.


#### __Returning players login__
Playing the official Wordle game the game recognises the devices, so as the player returns day after day it can track the player's stats. For extended features, players can register an account with New York Times to access other games too. The benefit is that a returning player can keep building on their winning streak to overcome their own high score (longest streak) without having to play more rounds in one single session of accessing the game.

__How might we create this?__
The most feasible way I can think of is to either:
- provide new players their timestamp based ID after entering their name so that next time they access the game, if it is entered in the name prompt of the welcome page, the game can recognise the input is all numeric and 12 digits long, which makes the game lookup the number as an ID, if it exists in our worksheet it will pull the data into the game and allow the next round, if won to increment the current winning streak as if the player had not closed the previous game.
- or that when new players enter their name on the welcome page prompt, the game asks the player to provide a unique username and password, with the game confirming that the username is valid and available in the worksheet. Next time the player returns, when prompted for a name, the player can enter their username, the game looks up the usernames in the worksheet and prompts for a password, before it resumes the game with the same stats.  -->

### Data Models
Chefs on the Net app uses a relational database to store and manage data. The relational database management system software used was PostgreSQL and was hosted on [Code Institute service](https://dbs.ci-dbs.net/).

#### Entity Relationship Diagram

![Entity Relationship Diagram](docs/images/RecipeBook_ERD.jpg)

## Technologies
- Languages used:
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - [Django](https://docs.djangoproject.com/en/5.0/)
- [Draw.io](https://app.diagrams.net/#) - a free web-based diagram drawing tool.
- [GitPod](https://www.gitpod.io/) - Cloud-based IDE to edit code and Git version control.
- [GitHub](https://github.com/) - to store and publish the project.
- [Am I Responsive](https://ui.dev/amiresponsive) - to visualise the website in various display sizes.
- [PEP8 guide](https://peps.python.org/pep-0008/) - for guidance on python formatting standards. 
- [Code Institute's Python linter](https://pep8ci.herokuapp.com/) - to validate the Python code. 
- [Heroku](https://dashboard.heroku.com/) - for deployment of our web app.

## Testing 

### Validator Testing 

- HTML
  - No errors were returned when passing through the official, just warnings on use of aria-labels on span elements. These span elements are the cards in the first step of the "How To Play" breaking down the value each card has, aria labels were added to make the site more accessible with the ability to describe the value of the card. [W3C validator](https://validator.w3.org/nu/)<br>
  ![HTML valid screenshot](docs/images/html-validation.PNG)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)<br>
  ![CSS valid screenshot](docs/images/css-validation.PNG) 
- JavaScript
  - No errors were found when passing through [JS hint error checker](https://jshint.com/)<br>
  ![JS error free screenshot](docs/images/js-validation.PNG)
- Python
  - No errors were found [Code Institute's Python linter](https://pep8ci.herokuapp.com/) - to validate the Python code.<br>
  ![Python error free screenshot](docs/images/pi-linter.PNG)

- Accessibility
  - Running the site through lighthouse analysis does show some issues with some insuficient colour contrast and performance suggests I should minimise my JS files for faster loading. Otherwise still rates above 90 on accessibility:
    - Mobile:<br>
  ![Lighthouse mobile analysis](docs/images/lighthouse-test-mobile.PNG)
 
    - Desktop:<br>
  ![Lighthouse desktop analysis](docs/images/lighthouse-test.PNG)

  - Running the site through [WAVE accessibility tool](https://wave.webaim.org/report#/https://dasic002.github.io/GameOfKings/index.html) showed no obvious errors after some improvements were made.<br>
  ![Wave accessibility evaluation results](documentation/Test-wave-accessibility.PNG)



### Manual Testing

#### Devices and browsers used
- iPhone 12 Pro - iOS 18.1.1
  - Safari (v18.1.1)
  - Chrome (v131)

- iPad Pro (12.9 inch - 4th Gen) - iPadOS 18.1.1
  - Safari (v18.1.1)
  - Chrome (v131)

- Dell Precision 3510 laptop - Windows 10 Pro (2H22)
  - Chrome (v131)

#### Manual testing checklist

| Feature | Action | Expected Behaviour | Pass/Fail | Notes |
|-|-|-|-|-|
|Google fonts|Loading the page|Google fonts load|PASS|
|Font awesome icons|Loading the page|Icons appear as intended|PASS|
|Images|Loading the page|images appear as intended|PASS|
|content text |Loading the page|text appears as intended|PASS|
|Nav bar appearance|Loading the page|Nav bar appears as expected, collapsed hamburger icon for narrow displays|PASS|
|Nav Button - hamburger icon|Click Hamburger icon|hamburger icon toggles to reveal and collapse nav menu|PASS|
|Nav button - Register|Click button "Register" just after loading the site|Loads sign up page|PASS|
|Nav button - Login|Click button "Login" just after loading the site|Loads login page|PASS|
|Nav button - Logout|Click button "Logout" after starting a game|Loads logout confirmation page|PASS|
|Nav Button - Logout|Click button "Sign out"|Confirms logging out and returns to Home page|PASS|
|Nav Button - Home|Click button "Home"|Loads to Home as either welcome or library dependant on login status|PASS|
|Nav Button - My Recipes|Click button "My Recipes"|Loads Logged in user's recipe library to view and manage their recipes|PASS|
|Page scaling - mobile|Viewing the page on mobile display in portrait|Font size is legible and the page does not require scrolling on timed buttons. No overlapping text or images.|PASS|
|Page scaling - mobile|Viewing the page on mobile display in landscape|Font size scales down to fit in the height of the display. Page includes left and right margins to keep content in the centre still.|PASS|
|Page scaling - desktop|Viewing the page on a desktop/laptop display in landscape with the browser taking the width of the display|Font size scales down to fit in the height of the display. Page includes left and right margins to keep content in the centre still.|PASS|
|Page scaling - desktop|Viewing the page on a desktop/laptop display in landscape with the browser taking the width of the display|Font size scales down to fit in the height of the display. Page includes left and right margins to keep content in the centre still.|PASS|
|Error 403 page|Enter existing url user is not allowed to access for the site|Calls up custom 403.html|PASS|
|Error 403 page|Click on the Home button|Brings viewer back to main page|PASS|
|Error 404 page|Enter non-existing url for the site|Calls up custom 404.html|PASS|
|Error 404 page|Click on the Home button|Brings viewer back to main page|PASS|
|Error 500 page|Browse site when a function in view has been disabled|Calls up custom 500.html|PASS|
|Error 500 page|Click on the Home button|Brings viewer back to main page|PASS|



### Bugs

<!-- - __ANSI escape 8-bit colours not visible on Heroku - FIXED__<br>
Heroku allows for colours in its app, but these are restricted to 3-bit and 4-bit, so have selected colours from that selection instead.

- __Dictionary includes words with the character "ƒ" - FIXED__<br>
This character appeared on words that should have ended with an accented e (é), like __sauté__. For ease of playing the game this character has been replaced with a plain "e". -->


## Deployment
### Local Development

#### Forking the Repository

- Log in to GitHub.
- Go to the repository for this project (<https://github.com/dasic002/virtual_recipe_book>).
- In the top-right corner of the page, click "Fork".
- Under "Owner", select an owner for the repository from the dropdown menu.
- Optionally, in the "Description" field, type a description of your fork.
- To copy the main branch only, select the "Copy the main branch only" check box. If you do not select this option, all branches will be copied into the new fork.
- Click "Create fork"

#### Cloning Your Forked Repository

- Log-in to GitHub.com, navigate to your fork of the repository.
- Above the list of files, click Code.
- Copy the URL for the repository.
  - To clone the repository using HTTPS, under "Clone with HTTPS", click the "Copy" icon.
  - To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click the "Copy" icon.
  - To clone a repository using GitHub CLI, click Use GitHub CLI, then click the "Copy" icon.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the URL you copied earlier.
- Press Enter. Your local clone will be created.

For more details about forking and cloning a repository, please refer to [GitHub documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

#### Install Dependencies

Use the `pip install -r requirements.txt` command to install all of the Python modules and packages listed in your requirements.txt file.

#### Create your env.py

- In your project workspace, create a file called env.py and make sure this file is included in the .gitignore file.
- Add the following code:

```python
import os

os.environ["DATABASE_URL"]='<copiedURL>'
os.environ['SECRET_KEY'] = '<ADD YOUR SECRET KEY HERE>'
os.environ['CLOUDINARY_URL'] = '<API ENVIRONEMENT VARIABLE>'

```

- Replace `<ADD YOUR SECRET KEY HERE>` in the SECRET_KEY environment variable with your own secret key.
- Save the file.

#### Create a Database

- Create an account and log in with ElephantSQL.com.
- From the dashboard click “Create New Instance”.
- Set up your plan
  - Give your plan a Name
  - Select a plan tier
  - You can leave the Tags field blank
- Select “Select Region”
- Select a data center near you
- Then click “Review”
- Check your details are correct and then click “Create instance”
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, click the copy icon to copy the database URL
- In your env.py file replace `<copiedURL>` in the DATABASE_URL environment variable with the copied URL.
- Save the file.

#### Set Up Cloudinary

- Create an account and log in with Cloudinary.com.
- In the dashboard copy your API Environment variable.
- In your env.py file replace `<API ENVIRONEMENT VARIABLE>` in the CLOUDINARY_URL environment variable with the copied API Environment variable.
- Save the file.

### Deployment

- The requirements.txt file in the project was updated to include details on the project dependencies. Steps to do this are :
  - Enter the following command at the terminal prompt : "pip3 freeze > requirements.txt"
  - Commit changes to requirements.txt and push to GitHub.
- In `setting.py`, add Heroku Hostname to ALLOWED_HOSTS.

```python
ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "YOUR_HOSTNAME"]
```

- Make surea file named Procfile exists on the top level directory which contans the following code:

```python
web: gunicorn PROJECT_NAME.wsgi
```

- Commit changes and push to GitHub.
- Log in to Heroku, create an account if necessary.
- From the Heroku dashboard, click "Create new app". For a new account a button will be displayed on screen, if you already have one or more apps created a link to this function is located in the "New" dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region. Then click Create app.
- Select the "settings" tab and click the "Reveal Config Vars" button.
- Enter the following values into the specified fields and click "Add":

    | KEY | VALUE |
    |-----|-------|
    | CLOUDINARY_URL | paste your API Environment variable copied from the Cloudinary dashboard |
    | DATABASE_URL | paste the URL copied from ElephantSQL dashboard |
    | SECRET_KEY | paste your secret key |

- Select the "Deploy" tab.
- Select GitHub as the Deployment Method and click "Connect to GitHub".
- Enter the name of your GitHub repository in the search bar and click "Search".
- Click the "Connect" button to link your GitHub repository with your Heroku app.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy.
- The application can be run from the Application Configuration page by clicking on the Open App button.


## Credits 

### Media
- [Am I Responsive](https://ui.dev/amiresponsive) - to visualise the website in various display sizes as the preview used in this readme file.

### Code

<!-- - Reference for clearing the screen in python - [Clearing Screen in Linux Operating System](https://www.geeksforgeeks.org/clear-screen-python/)
- Reference for multiline string to print "pages" - [Multiline Strings](https://www.w3schools.com/python/gloss_python_multi_line_strings.asp)
- Reference for readlines() method to list words - [readlines() Method](https://www.w3schools.com/python/ref_file_readlines.asp)
- Validating input - [Love Sandwiches - Validating our data part 1](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/?child=first)
- Reference for alphabetic chars only in a string - [String isalpha() Method](https://www.w3schools.com/python/ref_string_isalpha.asp)
- Reference to check value exists in list - [Check If List Item Exists](https://www.w3schools.com/python/gloss_python_check_if_list_item_exists.asp)
- Reference for while loop until valid data - [Creating our User Request Loop](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/?child=first)
- Reference for centering text in string - [String center() Method](https://www.w3schools.com/python/ref_string_center.asp)
- Reference to create dictionary comprehensions - [Dictionary comprehensions](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/f780287e5c3f4e939cd0adb8de45c12a/82a59be9f20a4f36bff58ff4a102d60a/)
- Formatting text - [How do I print colored text to the terminal?](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
- ANSI colours - [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit)
- Reference for Datetime to use in creating a timestamp based ID - [Datetime](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/272f493b4d57445fbd634e7ceca3a98c/4ab3e01af44f4bf2828739c1d0591a45/) and [formatting](https://www.w3schools.com/python/python_datetime.asp#gsc.tab=0)
- Reference for getting values from a dictionary - [values()](https://www.w3schools.com/python/ref_dictionary_values.asp)
- Reference for returning a sum of integers in a list - [math.fsum()](https://www.w3schools.com/python/ref_math_fsum.asp)
- Reference for setup, finding and updating spreadsheet with [gspread](https://docs.gspread.org/en/latest/user-guide.html) -->

### Acknowledgement
- My mentor Brian Macharia for his insight, guidance and words of encouragement.

<!--## Other General Project Advice

 Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process!  -->

